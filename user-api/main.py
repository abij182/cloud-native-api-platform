
import os

from fastapi import FastAPI

APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(
    title="User API",
    description="User microservice for the DevOps portfolio project",
    version=APP_VERSION,
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/api/info")
def get_api_info():
    return {
        "application": "User API",
        "environment": APP_ENV,
        "version": APP_VERSION,
    }


@app.get("/api/users")
def get_users():
    return [
        {"id": 1, "name": "Abishek", "email": "abishek@example.com"},
        {"id": 2, "name": "Rahul", "email": "rahul@example.com"},
    ]


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Sample User",
        "email": "user@example.com",
    }