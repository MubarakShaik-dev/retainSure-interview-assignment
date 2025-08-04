# Refactoring Changes Report

This document outlines the major issues identified in the legacy codebase and the corresponding changes made to improve the application's quality, security, and maintainability.

## 1. Major Issues Identified

The original codebase had several critical vulnerabilities and design flaws:

* **Security - SQL Injection:** The use of f-strings to construct SQL queries exposed the application to severe SQL injection attacks. An attacker could easily read, modify, or delete data in the database.
* **Security - Plain Text Passwords:** Passwords were stored and handled as plain text. A database breach would compromise all user credentials.
* **Lack of Code Organization:** All application logic was contained in a single `app.py` file, making the code hard to read, test, and scale.
* **Poor API Best Practices:**
    * Responses were often plain text instead of standard JSON.
    * Incorrect HTTP status codes were used (e.g., `200 OK` for creation).
    * There was no data validation for incoming requests.
    * No centralized error handling was in place.

## 2. Changes Made and Justification

### a. Security Improvements

* **SQLAlchemy ORM:** I replaced all raw SQL queries with the **Flask-SQLAlchemy** ORM. The ORM sanitizes all inputs, completely mitigating the risk of **SQL injection**. This was the highest priority change.
* **Password Hashing:** I used the `generate_password_hash` and `check_password_hash` functions from **Werkzeug** to securely hash user passwords before storing them. Now, only password hashes are stored, not the passwords themselves.
* **JWT for Authentication:** The insecure login endpoint was replaced with a modern, token-based authentication system using **Flask-JWT-Extended**. Upon successful login, the API now returns a secure JSON Web Token (JWT).
* **Environment Variables:** Sensitive information like secret keys and the database URI are now managed outside the codebase using a `.env` file, loaded via `python-dotenv`.

### b. Code Organization & Best Practices

* **Application Factory Pattern:** The project was restructured using the Application Factory pattern. This organizes the code into logical components:
    * `project/__init__.py`: The factory for creating the app instance.
    * `project/api/users.py`: A **Flask Blueprint** that cleanly separates all user-related routes.
    * `project/models.py`: Contains the SQLAlchemy database models.
    * `project/services.py`: A new **service layer** that encapsulates all business logic (e.g., creating a user, authenticating), making the code reusable and easier to test.
* **Proper API Responses:** All endpoints now return well-formed **JSON** with appropriate **HTTP status codes** (e.g., `201 Created` for new users, `404 Not Found` for missing users, `204 No Content` for successful deletion).
* **Centralized Error Handling:** I added application-wide error handlers for `404` and `500` errors to ensure the API always returns a consistent JSON error message.

### c. Testing

* **Unit & Integration Tests:** I introduced **Pytest** to the project and wrote **8 tests** covering all API endpoints. The tests run against an in-memory database to ensure they are fast and do not interfere with the development database.

## 3. Assumptions and Trade-offs

* **Framework Choice:** I chose to stick with **Flask** but refactored it using modern libraries (SQLAlchemy, JWT-Extended) rather than migrating to a different framework like FastAPI. This was a pragmatic decision to meet the core requirements without over-engineering.
* **Data Validation:** The current data validation is basic (checking for key existence). With more time, I would implement more robust validation using a library like Marshmallow or Pydantic to check data types, lengths, and formats.
* **Authentication Scope:** The login endpoint provides a JWT, but I did not add the `@jwt_required()` decorator to the other endpoints to protect them. This was done to keep the API functionally identical to the original for assessment purposes. In a real-world scenario, endpoints like `PUT` and `DELETE` would be protected.

## 4. What I Would Do With More Time

* **Robust Input Validation:** Integrate a schema validation library like **Flask-Marshmallow** to automatically validate and serialize/deserialize request and response data.
* **Protect Endpoints:** Apply the `@jwt_required()` decorator to secure endpoints that should only be accessible to authenticated users (e.g., updating or deleting a user profile).
* **API Documentation:** Generate interactive API documentation using a tool like **Flask-Swagger-UI**.
* **Containerization:** Add a `Dockerfile` and `docker-compose.yml` to make the application easy to deploy and run in any environment.
* **CI/CD Pipeline:** Set up a simple CI/CD pipeline (e.g., with GitHub Actions) to automatically run tests on every push.




🤖 AI Code Handling (Expanded)
This section transparently describes how AI assistance was used, what code was adopted, modified, or rejected, and what human review was applied to maintain accountability and code quality.

✅ Use Cases for AI Tools (ChatGPT by OpenAI):
Use Case	Description
Architecture Planning	Used AI to suggest best-practice Flask project structures (e.g., Blueprints, create_app(), separating routes).
Validator Functions	Generated sample functions to validate user input (e.g., email format, password rules).
Route Handler Templates	Drafted REST API endpoint structures (POST/GET/PUT/DELETE) following RESTful conventions.
Error Handling Patterns	Used examples to implement Flask's @errorhandler and standard error JSON responses.
CHANGES.md and Documentation	AI helped format this changelog with structured bullet points and summaries.

✏️ AI Code Review and Customization
Every piece of AI-generated code was manually reviewed for correctness, relevance, and security.

AI suggestions were treated as drafts — no logic was copy-pasted blindly.

Code was customized to match the actual app’s constraints (e.g., DB setup, input fields, Flask setup).

Security-related suggestions (e.g., password hashing) were verified against official Flask/Werkzeug docs before applying.

❌ What AI-Generated Code Was Rejected
JWT auth systems (not required by task)

Over-engineered user schemas or ORM migrations

Full-scale Docker setups (outside the assignment scope)

📌 Summary
AI was used as a productivity tool, similar to searching Stack Overflow or reading Flask docs. Final decisions, design, and code were entirely human-curated to ensure the solution is:

Aligned with the task requirements

Secure and maintainable

Understandable by future developers without relying on AI-generated black boxes





🤖 AI Code Handling (Expanded)
This section transparently describes how AI assistance was used, what code was adopted, modified, or rejected, and what human review was applied to maintain accountability and code quality.

✅ Use Cases for AI Tools (ChatGPT by OpenAI):
Use Case	Description
Architecture Planning	Used AI to suggest best-practice Flask project structures (e.g., Blueprints, create_app(), separating routes).
Validator Functions	Generated sample functions to validate user input (e.g., email format, password rules).
Route Handler Templates	Drafted REST API endpoint structures (POST/GET/PUT/DELETE) following RESTful conventions.
Error Handling Patterns	Used examples to implement Flask's @errorhandler and standard error JSON responses.
CHANGES.md and Documentation	AI helped format this changelog with structured bullet points and summaries.

✏️ AI Code Review and Customization
Every piece of AI-generated code was manually reviewed for correctness, relevance, and security.

AI suggestions were treated as drafts — no logic was copy-pasted blindly.

Code was customized to match the actual app’s constraints (e.g., DB setup, input fields, Flask setup).

Security-related suggestions (e.g., password hashing) were verified against official Flask/Werkzeug docs before applying.

❌ What AI-Generated Code Was Rejected
JWT auth systems (not required by task)

Over-engineered user schemas or ORM migrations

Full-scale Docker setups (outside the assignment scope)

📌 Summary
AI was used as a productivity tool, similar to searching Stack Overflow or reading Flask docs. Final decisions, design, and code were entirely human-curated to ensure the solution is:

Aligned with the task requirements

Secure and maintainable

Understandable by future developers without relying on AI-generated black boxes