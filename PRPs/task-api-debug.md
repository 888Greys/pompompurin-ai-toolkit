# Task API Debug Guide - Root Cause Analysis

## Common Issues and Solutions

### 1. Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'app'`

**Root Cause**: Python path not configured correctly

**Solution**:
```bash
# Run from the task-api directory
cd task-api
export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn app.main:app --reload
```

### 2. Database Connection Issues

**Symptom**: `sqlite3.OperationalError: no such table: users`

**Root Cause**: Database tables not created

**Solution**:
```python
# In app/main.py, ensure this line exists:
models.Base.metadata.create_all(bind=engine)
```

### 3. Authentication Failures

**Symptom**: `401 Unauthorized` on protected endpoints

**Root Cause Analysis**:
1. **Invalid Token**: Check token format and expiration
2. **Missing Header**: Ensure `Authorization: Bearer <token>` header
3. **Wrong Secret**: Verify SECRET_KEY in auth.py

**Debug Steps**:
```bash
# Test token generation
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=test@example.com&password=testpass"

# Verify token in JWT debugger at jwt.io
```

### 4. Validation Errors

**Symptom**: `422 Unprocessable Entity`

**Root Cause**: Pydantic validation failures

**Debug Process**:
1. Check request body format
2. Verify required fields
3. Validate data types
4. Check enum values (status, priority)

**Example Fix**:
```json
// Wrong
{
  "title": "",  // Empty string not allowed
  "status": "invalid_status"  // Not in enum
}

// Correct
{
  "title": "Valid task title",
  "status": "todo",
  "priority": "medium"
}
```

### 5. CORS Issues

**Symptom**: Browser blocks requests with CORS error

**Root Cause**: CORS middleware not configured properly

**Solution**:
```python
# In app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 6. Test Failures

**Symptom**: Tests fail with database errors

**Root Cause**: Test database conflicts

**Solution**:
```bash
# Clean test database
rm test.db

# Run tests with fresh database
pytest tests/ -v
```

## Performance Issues

### 1. Slow Database Queries

**Diagnosis**:
```python
# Add logging to see query performance
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

**Solutions**:
- Add database indexes
- Implement query optimization
- Use database connection pooling

### 2. Memory Leaks

**Diagnosis**:
```python
# Monitor database connections
from sqlalchemy import event
from sqlalchemy.engine import Engine

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    print(f"New connection: {id(dbapi_connection)}")
```

## Security Issues

### 1. JWT Token Security

**Best Practices**:
- Use strong SECRET_KEY (environment variable)
- Implement token refresh mechanism
- Add token blacklist for logout
- Set appropriate expiration times

### 2. Password Security

**Verification**:
```python
# Test password hashing
from app.auth import get_password_hash, verify_password

password = "testpass"
hashed = get_password_hash(password)
print(f"Hash: {hashed}")
print(f"Verify: {verify_password(password, hashed)}")
```

## Monitoring and Logging

### 1. Add Request Logging

```python
# In app/main.py
import logging
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.2f}s")
    return response
```

### 2. Health Check Monitoring

```bash
# Monitor API health
curl http://localhost:8000/health

# Expected response
{"status": "healthy"}
```

## Deployment Issues

### 1. Environment Variables

**Production Checklist**:
- [ ] Set SECRET_KEY from environment
- [ ] Configure database URL
- [ ] Set CORS origins
- [ ] Enable HTTPS
- [ ] Configure logging level

### 2. Database Migration

```python
# For production, use Alembic for migrations
pip install alembic
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Testing Strategies

### 1. Unit Test Coverage

```bash
# Generate coverage report
pytest tests/ --cov=app --cov-report=html --cov-report=term-missing
```

### 2. Integration Testing

```bash
# Test full API workflow
python -m pytest tests/ -v -k "test_full_workflow"
```

### 3. Load Testing

```bash
# Install locust for load testing
pip install locust

# Create locustfile.py for API load testing
```

## Quick Fixes Checklist

When something breaks:

1. **Check Logs**: Look for error messages and stack traces
2. **Verify Environment**: Ensure all dependencies installed
3. **Test Database**: Verify database connection and tables
4. **Check Authentication**: Test login flow manually
5. **Validate Input**: Ensure request format matches schema
6. **Review Recent Changes**: Check git diff for breaking changes
7. **Run Tests**: Execute test suite to identify failures
8. **Check Documentation**: Verify API contract compliance

## Emergency Recovery

### 1. Reset Database
```bash
rm task_management.db test.db
python -c "from app.database import engine; from app.models import Base; Base.metadata.create_all(bind=engine)"
```

### 2. Restart Service
```bash
pkill -f uvicorn
uvicorn app.main:app --reload --port 8000
```

### 3. Verify Service
```bash
curl http://localhost:8000/health
curl http://localhost:8000/docs
```