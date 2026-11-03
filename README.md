# CodeNova DevOps Portfolio

A Python FastAPI project demonstrating the four DevOps tasks assigned in CodeNova Batch 01.

[![Automated Tests](https://github.com/YOUR_GITHUB_USERNAME/codenova-devops-portfolio/actions/workflows/test.yml/badge.svg)](https://github.com/YOUR_GITHUB_USERNAME/codenova-devops-portfolio/actions/workflows/test.yml)

## Features
- FastAPI REST endpoints: `/`, `/health`, and `/greet/{name}`
- Automated tests with pytest
- Linting with Ruff
- GitHub Actions CI on pushes and pull requests
- Multi-stage Docker image running as a non-root user
- Sequential CI/CD workflow with optional Render deployment hook

## Tech stack
Python 3.12, FastAPI, pytest, Ruff, Git, GitHub Actions, Docker.

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Visit:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## Test and lint

```bash
pytest -v
ruff check .
```

## Docker

```bash
docker build -t codenova-devops-portfolio:latest .
docker run --rm -p 8000:8000 codenova-devops-portfolio:latest
```

## Git collaboration
See [Git workflow](docs/GIT_WORKFLOW.md) and [merge conflict exercise](docs/MERGE_CONFLICT.md).

## Docker documentation
See [Docker guide](docs/DOCKER_GUIDE.md).

## CI/CD documentation
See [CI/CD guide](docs/CICD_GUIDE.md). Add the GitHub Actions secret `RENDER_DEPLOY_HOOK_URL` to activate Render deployment.

## Project task mapping
- Task 1: Git and GitHub workflow
- Task 2: Automated testing pipeline
- Task 3: Dockerized application
- Task 4: CI/CD pipeline

## Screenshots and demo
Add genuine screenshots of successful test runs, GitHub Actions, Docker build/image inspection, and the live deployed application here before submission.

## Security
Do not commit API keys, passwords, deploy hooks, or other secrets.
