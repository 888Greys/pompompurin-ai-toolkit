# Task Management API

A comprehensive RESTful API for task management built with FastAPI, demonstrating the PRP (Product Requirement Prompt) methodology for AI-assisted development.

## Features

- **User Authentication**: JWT-based authentication system
- **Task Management**: Full CRUD operations for tasks
- **Data Validation**: Pydantic models for request/response validation
- **Database Integration**: SQLAlchemy ORM with SQLite
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation
- **Testing**: Comprehensive test suite with pytest

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the API

```bash
# Start the development server
uvicorn app.main:app --reload --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html
```

## API Usage Examples

### Register a User
```bash
curl -X POST "http://localhost:8000/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "securepass123"}'
```

### Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=securepass123"
```

### Create a Task
```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_TOKEN_HERE" \
     -d '{"title": "Complete project", "description": "Finish the API", "priority": "high"}'
```

### Get Tasks
```bash
curl -X GET "http://localhost:8000/tasks" \
     -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Project Structure

```
task-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── auth.py              # Authentication logic
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       └── tasks.py         # Task endpoints
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test configuration
│   ├── test_auth.py         # Authentication tests
│   └── test_tasks.py        # Task tests
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## PRP Methodology

This project was built using the PRP (Product Requirement Prompt) methodology, which combines:

1. **Comprehensive Context**: Detailed requirements and documentation
2. **Implementation Blueprint**: Step-by-step development plan
3. **Validation Loops**: Automated testing and quality checks

See the related PRP documents:
- `PRPs/task-api-planning.md` - High-level planning
- `PRPs/task-api-core.md` - Detailed implementation PRP
- `PRPs/task-api-contract.md` - API contract specification

## Development

### Adding New Features

1. Create a PRP document in the `PRPs/` directory
2. Follow the implementation blueprint
3. Run validation loops to ensure quality
4. Update tests and documentation

### Code Quality

The project follows these quality standards:
- Type hints with mypy
- Code formatting with black/ruff
- Comprehensive test coverage
- API documentation
- Security best practices

## Security

- Passwords are hashed using bcrypt
- JWT tokens for authentication
- SQL injection protection via ORM
- Input validation with Pydantic
- CORS configuration for cross-origin requests

## License

MIT License - see LICENSE file for details.