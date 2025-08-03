import string
import secrets
from urllib.parse import urlparse

# Use a cryptographically secure generator for random choices
_ALPHANUMERIC_CHARS = string.ascii_letters + string.digits

def generate_short_code(length: int = 6) -> str:
    """
    Generates a random alphanumeric short code of a given length.
    """
    return ''.join(secrets.choice(_ALPHANUMERIC_CHARS) for _ in range(length))

def is_valid_url(url: str) -> bool:
    """
    Validates if the given string is a well-formed URL.
    """
    if not isinstance(url, str) or not url:
        return False
    try:
        result = urlparse(url)
        # A valid URL must have a scheme (http, https) and a network location (domain)
        return all([result.scheme, result.netloc])
    except (ValueError, AttributeError):
        return False