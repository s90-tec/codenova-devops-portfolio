from fastapi import FastAPI

app = FastAPI(
    title="CodeNova DevOps Demo API",
    description="A small application for demonstrating Git, CI, Docker, and CI/CD.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the CodeNova DevOps Demo API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to CodeNova DevOps."}
@app.get("/about")
def about():
    return {
        "project": "CodeNova DevOps Portfolio",
        "purpose": "DevOps Internship Demonstration"
    }