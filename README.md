# CodeNova DevOps Portfolio

A Python FastAPI project demonstrating the four DevOps tasks assigned in CodeNova Batch 01.

[![Automated Tests](https://github.com/s90-tec/codenova-devops-portfolio/actions/workflows/test.yml/badge.svg)](https://github.com/s90-tec/codenova-devops-portfolio/actions/workflows/test.yml)
[![CI-CD Pipeline](https://github.com/s90-tec/codenova-devops-portfolio/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/s90-tec/codenova-devops-portfolio/actions/workflows/ci-cd.yml)

## Features
- FastAPI REST endpoints: `/`, `/health`, `/greet/{name}`, and `/about`
- Automated tests with pytest
- Linting with Ruff
- GitHub Actions CI on pushes and pull requests
- Multi-stage Docker image running as a non-root user
- Sequential CI/CD workflow with optional Render deployment hook

## Tech stack
Python 3.12 (CI and container), FastAPI, pytest, Ruff, Git, GitHub Actions, Docker.

## Architecture

```text
GitHub push / pull request
          |
          +--> Automated Tests: Ruff --> pytest
          |
          +--> main push CI/CD: Lint --> Test --> Docker build --> Render deploy hook
                                                                  |
                                                        FastAPI container :8000
```

The CI/CD deploy job requires the `RENDER_DEPLOY_HOOK_URL` repository secret. A missing secret fails deployment rather than reporting a successful deploy. No live URL is published until a deployment has been configured and its health endpoint verified.

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Visit:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## Test and lint

```bash
python -m pytest -v
python -m ruff check .
```

## Docker

```bash
docker build -t codenova-devops-portfolio:latest .
docker run --rm -p 8000:8000 codenova-devops-portfolio:latest
```

For image size, layers, and non-root-user verification, see [Docker guide](docs/DOCKER_GUIDE.md). Docker Desktop must be running before building locally.

## Git collaboration
See [Git workflow](docs/GIT_WORKFLOW.md) and the isolated [merge conflict exercise](docs/MERGE_CONFLICT.md).

## Docker documentation
See [Docker guide](docs/DOCKER_GUIDE.md).

## CI/CD documentation
See [CI/CD guide](docs/CICD_GUIDE.md). Configure a Render service and add the GitHub Actions secret `RENDER_DEPLOY_HOOK_URL` before merging a deployment-enabled change to `main`.

## Project task mapping
- Task 1: Git and GitHub workflow
- Task 2: Automated testing pipeline
- Task 3: Dockerized application
- Task 4: CI/CD pipeline

## Screenshots and demo
Capture genuine screenshots after running the corresponding steps: passing and deliberately failing tests, successful GitHub Actions runs, Docker build/image size/non-root inspection, and the deployed `/health` endpoint. Do not represent screenshots or a live URL as available until the checks have actually succeeded. See the task guides for the exact commands.

## Security
Do not commit API keys, passwords, deploy hooks, or other secrets.
