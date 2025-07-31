"""
CRUD (Create, Read, Update, Delete) operations for database entities.

This module contains all database operations, providing a clean interface
between the API endpoints and the database models.
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app import models, schemas


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hash.
    
    Args:
        plain_password: The plain text password to verify
        hashed_password: The hashed password to compare against
        
    Returns:
        True if password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    
    Args:
        password: The plain text password to hash
        
    Returns:
        The hashed password string
    """
    return pwd_context.hash(password)


# User CRUD operations
def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Get a user by ID.
    
    Args:
        db: Database session
        user_id: The user's ID
        
    Returns:
        User object if found, None otherwise
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    Get a user by email address.
    
    Args:
        db: Database session
        email: The user's email address
        
    Returns:
        User object if found, None otherwise
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Create a new user with hashed password.
    
    Args:
        db: Database session
        user: User creation schema with email and password
        
    Returns:
        The created user object
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> Optional[models.User]:
    """
    Authenticate a user by email and password.
    
    Args:
        db: Database session
        email: User's email address
        password: Plain text password
        
    Returns:
        User object if authentication successful, None otherwise
    """
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


# Task CRUD operations
def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[models.Task]:
    """
    Get tasks for a specific user with pagination.
    
    Args:
        db: Database session
        user_id: The user's ID
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return
        
    Returns:
        List of task objects
    """
    return (
        db.query(models.Task)
        .filter(models.Task.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_task(db: Session, task_id: int, user_id: int) -> Optional[models.Task]:
    """
    Get a specific task by ID for a user.
    
    Args:
        db: Database session
        task_id: The task's ID
        user_id: The user's ID (for authorization)
        
    Returns:
        Task object if found and belongs to user, None otherwise
    """
    return (
        db.query(models.Task)
        .filter(models.Task.id == task_id, models.Task.user_id == user_id)
        .first()
    )


def create_task(db: Session, task: schemas.TaskCreate, user_id: int) -> models.Task:
    """
    Create a new task for a user.
    
    Args:
        db: Database session
        task: Task creation schema
        user_id: The user's ID
        
    Returns:
        The created task object
    """
    db_task = models.Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        user_id=user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(
    db: Session, 
    task_id: int, 
    task: schemas.TaskUpdate, 
    user_id: int
) -> Optional[models.Task]:
    """
    Update an existing task for a user.
    
    Args:
        db: Database session
        task_id: The task's ID
        task: Task update schema with new values
        user_id: The user's ID (for authorization)
        
    Returns:
        Updated task object if found and belongs to user, None otherwise
    """
    db_task = get_task(db, task_id, user_id)
    if not db_task:
        return None
    
    # Update only provided fields
    update_data = task.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, user_id: int) -> Optional[models.Task]:
    """
    Delete a task for a user.
    
    Args:
        db: Database session
        task_id: The task's ID
        user_id: The user's ID (for authorization)
        
    Returns:
        Deleted task object if found and belongs to user, None otherwise
    """
    db_task = get_task(db, task_id, user_id)
    if not db_task:
        return None
    
    db.delete(db_task)
    db.commit()
    return db_task