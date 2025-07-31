"""
Pydantic schemas for request/response validation.

This module defines the data models used for API requests and responses,
providing automatic validation, serialization, and documentation.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models import TaskStatus, TaskPriority


# User Schemas
class UserBase(BaseModel):
    """Base user schema with common fields."""
    email: EmailStr


class UserCreate(UserBase):
    """Schema for user creation requests."""
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long")


class User(UserBase):
    """Schema for user responses."""
    id: int
    created_at: datetime
    
    class Config:
        """Pydantic configuration for ORM compatibility."""
        from_attributes = True


# Task Schemas
class TaskBase(BaseModel):
    """Base task schema with common fields."""
    title: str = Field(..., min_length=1, max_length=200, description="Task title cannot be empty")
    description: Optional[str] = Field(None, max_length=1000, description="Optional task description")
    priority: TaskPriority = TaskPriority.MEDIUM


class TaskCreate(TaskBase):
    """Schema for task creation requests."""
    pass


class TaskUpdate(BaseModel):
    """Schema for task update requests."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None


class Task(TaskBase):
    """Schema for task responses."""
    id: int
    status: TaskStatus
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        """Pydantic configuration for ORM compatibility."""
        from_attributes = True


# Authentication Schemas
class Token(BaseModel):
    """Schema for JWT token responses."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Schema for token payload data."""
    email: Optional[str] = None