# RAG Query API

This project exposes a simple FastAPI application used to query a small knowledge base.

## Endpoints

- `POST /query` – main endpoint for asking questions.
- `POST /api` – alias for `/query` (useful when clients expect `/api`).
- `GET /health` – returns the state of the database and whether the API key is set.
- `GET /` – returns a short message describing available endpoints.

Requests are handled by `app.py` and the service reads from `knowledge_base.db`.
Make sure to populate the database using `preprocess.py` before querying.
If your knowledge_base.db exceeds GitHub's 25 MB upload limit, see large_files/README.md for using Git LFS.
