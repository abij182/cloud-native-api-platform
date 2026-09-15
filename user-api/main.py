from fastapi import FastAPI

app = FastAPI(
    title="User API",
    description="User microservice for the DevOps portfolio project",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/users")
def get_users():
    return [
        {
            "id": 1,
            "name": "Abishek",
            "email": "abishek@example.com"
        },
        {
            "id": 2,
            "name": "Rahul",
            "email": "rahul@example.com"
        }
    ]


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Sample User",
        "email": "user@example.com"
    }