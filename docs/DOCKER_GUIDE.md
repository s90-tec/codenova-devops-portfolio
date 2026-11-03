# Docker Guide

Build:

```bash
docker build -t codenova-devops-portfolio:latest .
```

Run:

```bash
docker run --rm -p 8000:8000 codenova-devops-portfolio:latest
```

Open `http://localhost:8000/health`.

Inspect image size:

```bash
docker image ls codenova-devops-portfolio
```

Verify the runtime user:

```bash
docker run --rm --entrypoint id codenova-devops-portfolio:latest
```

The application should run as the non-root `appuser`.
