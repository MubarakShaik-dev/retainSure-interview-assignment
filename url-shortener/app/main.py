from flask import Flask, request, jsonify, redirect, Response
from werkzeug.exceptions import NotFound, BadRequest

from app.storage import URLStore
from app.utils import generate_short_code, is_valid_url

# Initialize the Flask application
app = Flask(__name__)

# Create a single, shared instance of our in-memory store
url_store = URLStore()

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """
    Creates a short URL for a given long URL.
    """
    data = request.get_json()
    if not data or 'url' not in data:
        raise BadRequest("Request body must be JSON and include a 'url' key.")

    original_url = data['url']
    if not is_valid_url(original_url):
        raise BadRequest(f"The provided URL is not valid: {original_url}")

    # Generate a unique short code
    while True:
        short_code = generate_short_code()
        if url_store.save_url(short_code, original_url):
            break
            
    short_url = request.host_url + short_code

    return jsonify({
        "short_code": short_code,
        "short_url": short_url
    }), 201

@app.route('/<string:short_code>', methods=['GET'])
def redirect_to_url(short_code: str):
    """
    Redirects to the original URL associated with the short code.
    """
    original_url = url_store.get_url(short_code)

    if original_url is None:
        raise NotFound("The requested short code was not found.")

    # Track the redirect before sending the user to the destination
    url_store.increment_click_count(short_code)

    return redirect(original_url)

@app.route('/api/stats/<string:short_code>', methods=['GET'])
def get_url_stats(short_code: str):
    """
    Returns analytics for a given short code.
    """
    stats = url_store.get_stats(short_code)

    if stats is None:
        raise NotFound("The requested short code was not found.")
        
    # Format the response as required
    return jsonify({
        "url": stats["original_url"],
        "created_at": stats["created_at"].isoformat(),
        "clicks": stats["clicks"]
    })

# --- Error Handlers ---

@app.errorhandler(NotFound)
def handle_not_found(error: NotFound) -> Response:
    """Custom 404 error handler."""
    return jsonify({"error": error.description}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error: BadRequest) -> Response:
    """Custom 400 error handler."""
    return jsonify({"error": error.description}), 400

@app.errorhandler(Exception)
def handle_generic_error(error: Exception) -> Response:
    """Generic 500 error handler."""
    # Log the error for debugging in a real application
    # app.logger.error(f"An unexpected error occurred: {error}")
    return jsonify({"error": "An internal server error occurred."}), 500