import pytest
from src.auth import UserAuthenticator

def test_user_registration():
    auth = UserAuthenticator()
    assert auth.register("testuser", "password123") == True
    assert auth.register("testuser", "password456") == False  # Duplicate

def test_user_login():
    auth = UserAuthenticator()
    auth.register("testuser", "password123")
    assert auth.login("testuser", "password123") == True
    assert auth.login("testuser", "wrongpassword") == False