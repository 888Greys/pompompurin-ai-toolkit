# Task Management API Contract

## API Specification

### Base URL
```
http://localhost:8000
```

### Authentication
- **Type**: Bearer Token (JWT)
- **Header**: `Authorization: Bearer <token>`

## Endpoints

### Authentication Endpoints

#### POST /auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response (200):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "created_at": "2024-01-01T12:00:00Z"
}
```

**Error Responses:**
- `400`: Email already registered
- `422`: Validation error

#### POST /auth/login
Authenticate user and receive access token.

**Request Body (form-data):**
```
username: user@example.com
password: securepassword123
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Error Responses:**
- `401`: Incorrect email or password

### Task Endpoints (Protected)

#### GET /tasks
Retrieve user's tasks with pagination.

**Query Parameters:**
- `skip` (optional): Number of tasks to skip (default: 0)
- `limit` (optional): Maximum tasks to return (default: 100)

**Response (200):**
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the task management API",
    "status": "in_progress",
    "priority": "high",
    "user_id": 1,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:30:00Z"
  }
]
```

#### POST /tasks
Create a new task.

**Request Body:**
```json
{
  "title": "New task",
  "description": "Task description",
  "status": "todo",
  "priority": "medium"
}
```

**Response (200):**
```json
{
  "id": 2,
  "title": "New task",
  "description": "Task description",
  "status": "todo",
  "priority": "medium",
  "user_id": 1,
  "created_at": "2024-01-01T13:00:00Z",
  "updated_at": "2024-01-01T13:00:00Z"
}
```

#### GET /tasks/{task_id}
Retrieve a specific task.

**Response (200):**
```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the task management API",
  "status": "in_progress",
  "priority": "high",
  "user_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:30:00Z"
}
```

**Error Responses:**
- `404`: Task not found

#### PUT /tasks/{task_id}
Update an existing task.

**Request Body:**
```json
{
  "title": "Updated task title",
  "status": "done"
}
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Updated task title",
  "description": "Finish the task management API",
  "status": "done",
  "priority": "high",
  "user_id": 1,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T14:00:00Z"
}
```

#### DELETE /tasks/{task_id}
Delete a task.

**Response (200):**
```json
{
  "message": "Task deleted successfully"
}
```

**Error Responses:**
- `404`: Task not found

## Data Models

### User
```json
{
  "id": "integer",
  "email": "string (email format)",
  "created_at": "string (ISO datetime)"
}
```

### Task
```json
{
  "id": "integer",
  "title": "string (required)",
  "description": "string (optional)",
  "status": "enum: todo|in_progress|done",
  "priority": "enum: low|medium|high",
  "user_id": "integer",
  "created_at": "string (ISO datetime)",
  "updated_at": "string (ISO datetime)"
}
```

## Error Handling

### Standard Error Response
```json
{
  "detail": "Error message description"
}
```

### HTTP Status Codes
- `200`: Success
- `400`: Bad Request (validation errors, duplicate email)
- `401`: Unauthorized (invalid credentials, missing token)
- `404`: Not Found (task not found)
- `422`: Unprocessable Entity (validation errors)

## Rate Limiting
- No rate limiting implemented in current version
- Recommended: 100 requests per minute per user

## Security Considerations
- JWT tokens expire after 30 minutes
- Passwords are hashed using bcrypt
- CORS is configured (currently allows all origins for development)
- SQL injection protection via SQLAlchemy ORM