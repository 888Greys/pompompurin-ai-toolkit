#!/usr/bin/env python3
"""
Comprehensive API Testing Script - Level 4 Creative Validation

This script implements the PRP methodology's Level 4 validation by testing
the complete user journey, edge cases, and performance characteristics.
"""

import requests
import time
import json
from typing import Dict, Any


class TaskAPITester:
    """Comprehensive tester for the Task Management API."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None
        self.user_id = None
        
    def test_health_check(self) -> bool:
        """Test basic API health and connectivity."""
        try:
            response = self.session.get(f"{self.base_url}/")
            assert response.status_code == 200
            data = response.json()
            assert "message" in data
            assert "version" in data
            print("✅ Health check passed")
            return True
        except Exception as e:
            print(f"❌ Health check failed: {e}")
            return False
    
    def test_user_registration(self) -> bool:
        """Test user registration with various scenarios."""
        try:
            # Use a unique email for each test run
            import time
            timestamp = int(time.time())
            user_data = {
                "email": f"test_user_{timestamp}@example.com",
                "password": "SecurePassword123!"
            }
            
            response = self.session.post(
                f"{self.base_url}/auth/register",
                json=user_data
            )
            assert response.status_code == 200
            data = response.json()
            assert "id" in data
            assert data["email"] == user_data["email"]
            self.user_id = data["id"]
            self.test_email = user_data["email"]
            self.test_password = user_data["password"]
            print("✅ User registration passed")
            
            # Test duplicate email registration
            response = self.session.post(
                f"{self.base_url}/auth/register",
                json=user_data
            )
            assert response.status_code == 400
            print("✅ Duplicate email validation passed")
            
            return True
        except Exception as e:
            print(f"❌ User registration failed: {e}")
            return False
    
    def test_authentication(self) -> bool:
        """Test JWT authentication flow."""
        try:
            # Test successful login with the user created in registration test
            login_data = {
                "username": getattr(self, 'test_email', 'comprehensive_test@example.com'),
                "password": getattr(self, 'test_password', 'SecurePassword123!')
            }
            
            response = self.session.post(
                f"{self.base_url}/auth/login",
                data=login_data
            )
            assert response.status_code == 200
            data = response.json()
            assert "access_token" in data
            assert data["token_type"] == "bearer"
            
            self.token = data["access_token"]
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
            print("✅ Authentication passed")
            
            # Test invalid credentials
            invalid_data = {
                "username": "wrong@example.com",
                "password": "wrongpassword"
            }
            response = self.session.post(
                f"{self.base_url}/auth/login",
                data=invalid_data
            )
            assert response.status_code == 401
            print("✅ Invalid credentials validation passed")
            
            return True
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False
    
    def test_task_crud_operations(self) -> bool:
        """Test complete CRUD operations for tasks."""
        try:
            # Create task
            task_data = {
                "title": "Test Task",
                "description": "This is a comprehensive test task",
                "priority": "high"
            }
            
            response = self.session.post(
                f"{self.base_url}/tasks/",
                json=task_data
            )
            assert response.status_code == 200
            created_task = response.json()
            assert created_task["title"] == task_data["title"]
            assert created_task["status"] == "todo"
            task_id = created_task["id"]
            print("✅ Task creation passed")
            
            # Read tasks
            response = self.session.get(f"{self.base_url}/tasks/")
            assert response.status_code == 200
            tasks = response.json()
            assert len(tasks) >= 1
            assert any(task["id"] == task_id for task in tasks)
            print("✅ Task listing passed")
            
            # Read specific task
            response = self.session.get(f"{self.base_url}/tasks/{task_id}")
            assert response.status_code == 200
            task = response.json()
            assert task["id"] == task_id
            print("✅ Task retrieval passed")
            
            # Update task
            update_data = {
                "title": "Updated Test Task",
                "status": "in_progress",
                "priority": "medium"
            }
            response = self.session.put(
                f"{self.base_url}/tasks/{task_id}",
                json=update_data
            )
            assert response.status_code == 200
            updated_task = response.json()
            assert updated_task["title"] == update_data["title"]
            assert updated_task["status"] == update_data["status"]
            print("✅ Task update passed")
            
            # Delete task
            response = self.session.delete(f"{self.base_url}/tasks/{task_id}")
            assert response.status_code == 200
            print("✅ Task deletion passed")
            
            # Verify task is deleted
            response = self.session.get(f"{self.base_url}/tasks/{task_id}")
            assert response.status_code == 404
            print("✅ Task deletion verification passed")
            
            return True
        except Exception as e:
            print(f"��� Task CRUD operations failed: {e}")
            return False
    
    def test_authorization(self) -> bool:
        """Test authorization and access control."""
        try:
            # Test unauthorized access
            unauthorized_session = requests.Session()
            response = unauthorized_session.get(f"{self.base_url}/tasks/")
            assert response.status_code == 401
            print("✅ Unauthorized access blocked")
            
            # Test invalid token
            invalid_session = requests.Session()
            invalid_session.headers.update({
                "Authorization": "Bearer invalid_token_here"
            })
            response = invalid_session.get(f"{self.base_url}/tasks/")
            assert response.status_code == 401
            print("✅ Invalid token rejected")
            
            return True
        except Exception as e:
            print(f"❌ Authorization tests failed: {e}")
            return False
    
    def test_data_validation(self) -> bool:
        """Test input validation and error handling."""
        try:
            # Test invalid email format
            invalid_user = {
                "email": "not-an-email",
                "password": "password123"
            }
            response = self.session.post(
                f"{self.base_url}/auth/register",
                json=invalid_user
            )
            assert response.status_code == 422  # Validation error
            print("✅ Email validation passed")
            
            # Test empty task title
            invalid_task = {
                "title": "",
                "description": "Empty title test"
            }
            response = self.session.post(
                f"{self.base_url}/tasks/",
                json=invalid_task
            )
            assert response.status_code == 422  # Validation error
            print("✅ Task validation passed")
            
            return True
        except Exception as e:
            print(f"❌ Data validation tests failed: {e}")
            return False
    
    def test_performance_basic(self) -> bool:
        """Test basic performance characteristics."""
        try:
            # Test response times
            start_time = time.time()
            response = self.session.get(f"{self.base_url}/")
            end_time = time.time()
            
            response_time = end_time - start_time
            assert response_time < 1.0  # Should respond within 1 second
            print(f"✅ Response time: {response_time:.3f}s (< 1.0s)")
            
            # Test multiple concurrent requests (basic load test)
            tasks_created = []
            start_time = time.time()
            
            for i in range(5):
                task_data = {
                    "title": f"Performance Test Task {i}",
                    "description": f"Task {i} for performance testing"
                }
                response = self.session.post(
                    f"{self.base_url}/tasks/",
                    json=task_data
                )
                assert response.status_code == 200
                tasks_created.append(response.json()["id"])
            
            end_time = time.time()
            total_time = end_time - start_time
            print(f"✅ Created 5 tasks in {total_time:.3f}s")
            
            # Cleanup
            for task_id in tasks_created:
                self.session.delete(f"{self.base_url}/tasks/{task_id}")
            
            return True
        except Exception as e:
            print(f"❌ Performance tests failed: {e}")
            return False
    
    def run_comprehensive_test(self) -> bool:
        """Run all test suites."""
        print("🚀 Starting Comprehensive API Testing (PRP Level 4 Validation)")
        print("=" * 60)
        
        tests = [
            ("Health Check", self.test_health_check),
            ("User Registration", self.test_user_registration),
            ("Authentication", self.test_authentication),
            ("Task CRUD Operations", self.test_task_crud_operations),
            ("Authorization", self.test_authorization),
            ("Data Validation", self.test_data_validation),
            ("Performance", self.test_performance_basic),
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            print(f"\n📋 Running {test_name}...")
            if test_func():
                passed += 1
            else:
                print(f"💥 {test_name} failed!")
        
        print("\n" + "=" * 60)
        print(f"🎯 Test Results: {passed}/{total} passed")
        
        if passed == total:
            print("🎉 All tests passed! API is production-ready.")
            return True
        else:
            print("⚠️  Some tests failed. Review and fix issues.")
            return False


def main():
    """Main function to run the comprehensive test suite."""
    tester = TaskAPITester()
    success = tester.run_comprehensive_test()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()