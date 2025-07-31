# PRP: Task Management API Core Implementation

## Goal
Implement a complete RESTful API for task management with FastAPI, including CRUD operations, user authentication, and database integration.

## Why
- **Business Value**: Enable users to manage their tasks efficiently through a robust API
- **Technical Value**: Demonstrate production-ready API development with modern Python stack
- **Learning Value**: Showcase PRP methodology for complex backend development

## What
A fully functional task management API with the following capabilities:

### User-Visible Behavior
- Users can register and authenticate
- Users can create, read, update, and delete tasks
- Tasks have title, description, status, and priority
- API returns proper HTTP status codes and error messages
- API documentation available via Swagger UI

### Technical Requirements
- RESTful API design principles
- JWT-based authentication
- SQLite database with SQLAlchemy ORM
- Pydantic models for validation
- Comprehensive error handling
- API documentation with OpenAPI

### Success Criteria
- [ ] All CRUD endpoints functional
- [ ] Authentication system working
- [ ] Database operations reliable
- [ ] Input validation comprehensive
- [ ] Error handling robust
- [ ] API documentation complete
- [ ] Test coverage > 90%

## All Needed Context

### Documentation & References
- url: https://fastapi.tiangolo.com/tutorial/
  why: FastAPI fundamentals and best practices
  
- url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
  why: JWT authentication implementation
  
- url: https://docs.sqlalchemy.org/en/20/tutorial/
  why: SQLAlchemy 2.0 ORM patterns
  
- url: https://docs.pydantic.dev/latest/
  why: Data validation and serialization

### Project Structure
```
task-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app instance
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── auth.py              # Authentication logic
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Auth endpoints
│       └── tasks.py         # Task endpoints
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test configuration
│   ├── test_auth.py         # Auth tests
│   └── test_tasks.py        # Task tests
├── requirements.txt         # Dependencies
└── README.md               # Project documentation
```

### Known Gotchas
- **CRITICAL**: Use bcrypt for password hashing, never store plain text
- **CRITICAL**: Validate JWT tokens on every protected endpoint
- **CRITICAL**: Use SQLAlchemy sessions properly to avoid connection leaks
- **CRITICAL**: Handle database constraints and provide meaningful error messages
- **IMPORTANT**: Use dependency injection for database sessions
- **IMPORTANT**: Implement proper CORS configuration for frontend integration

### Dependencies
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
```

## Implementation Blueprint

### Step 1: Project Setup
```python
# Create project structure
mkdir -p task-api/app/routers task-api/tests
cd task-api

# Initialize files
touch app/__init__.py app/main.py app/database.py
touch app/models.py app/schemas.py app/crud.py app/auth.py
touch app/routers/__init__.py app/routers/auth.py app/routers/tasks.py
touch tests/__init__.py tests/conftest.py tests/test_auth.py tests/test_tasks.py
```

### Step 2: Database Models (app/models.py)
```python
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class TaskStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskPriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(TaskStatus), default=TaskStatus.TODO)
    priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    owner = relationship("User", back_populates="tasks")
```

### Step 3: Pydantic Schemas (app/schemas.py)
```python
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from app.models import TaskStatus, TaskPriority

# User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Task schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

class Task(TaskBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Auth schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
```

### Step 4: Authentication (app/auth.py)
```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

SECRET_KEY = "your-secret-key-here"  # In production, use environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user
```

### Step 5: CRUD Operations (app/crud.py)
```python
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import get_password_hash, verify_password

# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Task CRUD
def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.user_id == user_id).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate, user_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()
    if db_task:
        update_data = task.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
```

### Step 6: API Routes
Implement auth and task routers with proper error handling and validation.

### Step 7: Main Application
Configure FastAPI app with routers, middleware, and database initialization.

## Validation Loop

### Level 1: Syntax & Style
```bash
# Install dependencies
pip install -r requirements.txt

# Check syntax and formatting
python -m py_compile app/*.py
python -m py_compile app/routers/*.py
```

### Level 2: Unit Tests
```bash
# Run comprehensive test suite
pytest tests/ -v --cov=app --cov-report=html

# Specific test categories
pytest tests/test_auth.py -v
pytest tests/test_tasks.py -v
```

### Level 3: Integration Tests
```bash
# Start the server
uvicorn app.main:app --reload --port 8000

# Test endpoints manually
curl -X POST "http://localhost:8000/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "testpass123"}'

curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=test@example.com&password=testpass123"

# Test protected endpoints with token
curl -X GET "http://localhost:8000/tasks" \
     -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### Level 4: API Documentation
```bash
# Verify Swagger UI is accessible
open http://localhost:8000/docs

# Verify ReDoc is accessible
open http://localhost:8000/redoc
```

## Quality Checklist
- [ ] All endpoints implemented and functional
- [ ] Authentication system secure and working
- [ ] Database operations reliable with proper error handling
- [ ] Input validation comprehensive
- [ ] API documentation complete and accurate
- [ ] Test coverage > 90%
- [ ] Error responses meaningful and consistent
- [ ] Security best practices followed

**Confidence Score: 9/10** - Comprehensive context provided with detailed implementation blueprint and validation gates.