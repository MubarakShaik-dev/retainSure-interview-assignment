🛠️ How AI Helped
Purpose	Description
✅ Planning Project Structure	ChatGPT suggested modular file organization using routes, services, utils, and storage.
✅ Input Validation Logic	Provided examples using urlparse and regex to validate URLs before shortening.
✅ Route Templates	Gave example Flask route structures for POST /api/shorten, GET /<short_code>, etc.
✅ Error Handling Patterns	Showed how to return proper HTTP status codes and JSON messages.
✅ Testing Suggestions	Generated test cases for typical and edge scenarios using pytest.
✅ Documentation	Helped format CHANGES.md and describe the implementation cleanly and concisely.

✏️ What Was Modified or Customized
Every AI suggestion was critically reviewed.

All routes, logic, and validators were customized to fit the exact structure, constraints, and expectations of the assignment.

Security-related suggestions (e.g., thread safety, input validation) were verified with Python/Flask official documentation.

In some cases, AI-suggested code was replaced with simpler or more accurate alternatives.

Final decisions about design, naming conventions, data structures, and testing strategies were entirely made by the developer (me).

❌ What Was Rejected
AI-generated suggestions that were out of scope or unnecessarily complex were rejected, such as:

Using a database (e.g., SQLite/PostgreSQL) when the prompt required in-memory storage.

Implementing JWT or user-based access control.

Using third-party services or dependencies not listed in the original requirements.txt.

✅ Summary
AI was used to accelerate development and remove repetitive tasks, similar to referencing docs or Stack Overflow. Final code quality, correctness, simplicity, and alignment with the assignment goals were ensured through manual testing, debugging, and rework.

No AI-generated content was used without understanding, reviewing, and modifying it.
