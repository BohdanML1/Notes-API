Notes API

Notes API is a RESTful API for managing personal notes, built with Django REST Framework and JWT authentication. It's designed for easy testing and deployment with Docker.

🔹 Features

CRUD for notes: Create, retrieve, update, and delete notes

JWT Authentication: Secure access to protected endpoints

Swagger UI: Interactive API documentation for testing endpoints

Dockerized: Run locally without manual dependency installation

Pagination: Built-in support for listing notes with pagination

🔹 Tech Stack

Python 3.11

Django 5.x

Django REST Framework (DRF)

djangorestframework-simplejwt

drf-yasg (Swagger)

PostgreSQL (via Docker)

Docker & Docker Compose

🔹 API Endpoints
Method	Endpoint	Description
POST	/api/token/	Obtain JWT access and refresh tokens
POST	/api/token/refresh/	Refresh JWT token
GET	/api/notes/	List all notes
POST	/api/notes/	Create a new note
GET	/api/notes/{id}/	Retrieve a note by ID
PUT	/api/notes/{id}/	Update a note by ID
PATCH	/api/notes/{id}/	Partially update a note
DELETE	/api/notes/{id}/	Delete a note

Note: All endpoints require JWT authentication except token retrieval.

🔹 Getting Started
Run Locally with Docker
docker compose up --build


Server URL: http://localhost:8000/

Swagger UI: http://localhost:8000/swagger/

JWT Authorization in Swagger

Go to Swagger UI at http://localhost:8000/swagger/

Click Authorize (top-right)

Paste your token:

Bearer <your_access_token>


All subsequent requests will use this JWT automatically.

🔹 Author

Bohdan Melnichin – Python/Django developer
