# Task API Project Onboarding Guide

## Welcome to the Task Management API Project!

This guide will help you get up to speed with our PRP-driven development methodology and the Task Management API implementation.

## Project Overview

### What We Built
A production-ready RESTful API for task management featuring:
- JWT-based user authentication
- Full CRUD operations for tasks
- SQLAlchemy ORM with SQLite database
- Comprehensive test suite
- Auto-generated API documentation

### PRP Methodology
This project demonstrates the **Product Requirement Prompt (PRP)** methodology:
- **PRP = PRD + curated codebase intelligence + agent/runbook**
- Enables AI-assisted development with one-pass implementation success
- Comprehensive context and validation loops ensure quality

## Getting Started (30 minutes)

### Step 1: Environment Setup (10 minutes)
```bash
# Clone and navigate to project
cd /path/to/PRPs-agentic-eng/task-api

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import fastapi, sqlalchemy, pydantic; print('Dependencies OK')"
```

### Step 2: Run the API (5 minutes)
```bash
# Start development server
uvicorn app.main:app --reload --port 8000

# Verify in browser
open http://localhost:8000/docs
```

### Step 3: Test the API (10 minutes)
```bash
# Run test suite
pytest tests/ -v

# Test manual workflow
curl -X POST "http://localhost:8000/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"email": "onboarding@example.com", "password": "test123"}'
```

### Step 4: Explore Documentation (5 minutes)
- **API Docs**: http://localhost:8000/docs
- **PRP Documents**: `PRPs/task-api-*.md`
- **Code Structure**: Review `task-api/app/` directory

## Understanding the PRP Workflow

### 1. PRP Creation Process
```
Planning → Research → Context Gathering → Implementation Blueprint → Validation
```

**Example**: See `PRPs/task-api-core.md` for a complete PRP

### 2. Key PRP Components
- **Goal**: What we're building and why
- **Context**: Documentation, examples, gotchas
- **Implementation Blueprint**: Step-by-step plan
- **Validation Loop**: Executable tests and checks

### 3. Execution Process
1. **Load PRP**: Understand requirements and context
2. **ULTRATHINK**: Plan implementation approach
3. **Execute**: Build following the blueprint
4. **Validate**: Run all validation gates
5. **Complete**: Ensure all criteria met

## Code Architecture Deep Dive

### Project Structure
```
task-api/
├── app/
│   ├── main.py          # FastAPI app and configuration
│   ├── database.py      # Database setup and session management
│   ├── models.py        # SQLAlchemy ORM models
│   ├── schemas.py       # Pydantic validation schemas
│   ├── crud.py          # Database operations
│   ├── auth.py          # JWT authentication logic
│   └── routers/
│       ├── auth.py      # Authentication endpoints
│       └── tasks.py     # Task CRUD endpoints
└── tests/
    ├── conftest.py      # Test configuration and fixtures
    ├── test_auth.py     # Authentication tests
    └── test_tasks.py    # Task operation tests
```

### Key Design Patterns

#### 1. Dependency Injection
```python
# Database session injection
def get_tasks(db: Session = Depends(get_db)):
    # Function receives database session automatically
```

#### 2. Authentication Middleware
```python
# Protected endpoints
def create_task(current_user: User = Depends(get_current_user)):
    # Function receives authenticated user automatically
```

#### 3. Pydantic Validation
```python
# Automatic request/response validation
def create_task(task: TaskCreate) -> Task:
    # Input automatically validated against schema
```

## Development Workflow

### Adding New Features

#### 1. Create a PRP
```bash
# Copy template
cp PRPs/templates/prp_base.md PRPs/new-feature.md

# Fill in sections:
# - Goal: What you're building
# - Why: Business value
# - Context: Documentation and examples
# - Implementation: Step-by-step plan
# - Validation: Tests and checks
```

#### 2. Execute the PRP
```bash
# Use PRP runner (if available)
uv run PRPs/scripts/prp_runner.py --prp new-feature --interactive

# Or implement manually following the blueprint
```

#### 3. Validate Implementation
```bash
# Run validation gates from PRP
pytest tests/ -v
python -m py_compile app/*.py
curl -X GET http://localhost:8000/health
```

### Code Review Process

#### 1. Use Built-in Commands
```bash
# Review changes
git diff --staged

# Check code quality
python -m py_compile app/*.py
pytest tests/ -v
```

#### 2. Validation Checklist
- [ ] All tests pass
- [ ] Code follows project patterns
- [ ] API documentation updated
- [ ] Error handling implemented
- [ ] Security considerations addressed

## Common Tasks

### 1. Adding a New Endpoint
```python
# 1. Add to router (app/routers/tasks.py)
@router.get("/search")
def search_tasks(query: str, current_user: User = Depends(get_current_user)):
    # Implementation

# 2. Add CRUD operation (app/crud.py)
def search_tasks(db: Session, query: str, user_id: int):
    # Database query

# 3. Add test (tests/test_tasks.py)
def test_search_tasks(authenticated_client):
    # Test implementation
```

### 2. Modifying Database Schema
```python
# 1. Update model (app/models.py)
class Task(Base):
    # Add new field
    category = Column(String)

# 2. Update schema (app/schemas.py)
class TaskBase(BaseModel):
    category: Optional[str] = None

# 3. Update tests
# 4. Consider migration strategy for production
```

### 3. Adding Authentication Features
```python
# 1. Extend auth.py with new functions
# 2. Add routes to auth router
# 3. Update user model if needed
# 4. Add comprehensive tests
```

## Troubleshooting

### Common Issues
1. **Import Errors**: Ensure PYTHONPATH includes project root
2. **Database Issues**: Check if tables are created
3. **Auth Failures**: Verify JWT token format and expiration
4. **Test Failures**: Clean test database between runs

### Debug Resources
- **Debug Guide**: `PRPs/task-api-debug.md`
- **API Contract**: `PRPs/task-api-contract.md`
- **Logs**: Check uvicorn output for errors

## Best Practices

### 1. PRP Quality
- Include comprehensive context
- Make validation gates executable
- Reference existing patterns
- Plan for error handling

### 2. Code Quality
- Follow existing patterns
- Add type hints
- Write comprehensive tests
- Document complex logic

### 3. Security
- Never commit secrets
- Validate all inputs
- Use proper authentication
- Handle errors gracefully

## Next Steps

### For New Team Members
1. **Complete this onboarding** (you're here!)
2. **Read all PRP documents** in `PRPs/task-api-*.md`
3. **Implement a small feature** using PRP methodology
4. **Review existing code** to understand patterns
5. **Ask questions** and contribute improvements

### For the Project
1. **Add more features** using PRP methodology
2. **Improve test coverage** and validation
3. **Enhance documentation** based on team feedback
4. **Scale the architecture** for production use

## Resources

### Documentation
- **FastAPI**: https://fastapi.tiangolo.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **Pydantic**: https://docs.pydantic.dev/
- **pytest**: https://docs.pytest.org/

### Project Files
- **Planning**: `PRPs/task-api-planning.md`
- **Implementation**: `PRPs/task-api-core.md`
- **API Contract**: `PRPs/task-api-contract.md`
- **Debug Guide**: `PRPs/task-api-debug.md`

### Commands Available
- `/prp-base-create` - Create new PRPs
- `/prp-base-execute` - Execute existing PRPs
- `/review-general` - Code review
- `/debug-RCA` - Root cause analysis

Welcome to the team! 🚀