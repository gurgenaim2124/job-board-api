# Job Board API

This is a Django + DRF based Job Board API project. It allows Employers to post jobs and Job Seekers to apply for them.

## Tech Stack

* Python 3.13
* Django 6.0
* Django REST Framework
* drf-yasg (Swagger documentation)
* djangorestframework-simplejwt (JWT Authentication)
* PostgreSQL (or your preferred database)

## Project Structure

```
job-board-api/
├── core/                 # Django project settings & urls
├── users/                # Custom User model, registration, authentication
├── jobs/                 # Job postings model and API
├── applications/         # Job applications model and API
├── manage.py
```

## Features

* Custom User model with roles: `employer` and `job_seeker`
* Job posting CRUD for Employers
* Apply to jobs for Job Seekers
* JWT Authentication (Register/Login/Token Refresh)
* Role-based access control ready
* Swagger documentation for API

## Setup

1. Clone the repository

```bash
git clone <repo-url>
cd job-board-api
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Run server

```bash
python manage.py runserver
```

## API Endpoints

* `/api/users/register/` - Register new user (POST)
* `/api/users/login/` - Login (POST, returns JWT token)
* `/api/users/token/refresh/` - Refresh JWT token (POST)
* `/swagger/` - Swagger UI for API documentation

## Next Steps

* Implement full role-based permissions for Jobs and Applications
* Add tests for permissions and API endpoints
* Expand API features like filtering, searching, and pagination
