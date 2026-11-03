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

Inspect image size and layers:

```bash
docker image ls codenova-devops-portfolio:latest
docker history --no-trunc codenova-devops-portfolio:latest
```

Verify the runtime user:

```bash
docker run --rm --entrypoint id codenova-devops-portfolio:latest
```

The application should run as the non-root `appuser` (UID 10001). To verify the running container:

```bash
docker run -d --name codenova-demo -p 8000:8000 codenova-devops-portfolio:latest
curl --fail http://127.0.0.1:8000/health
docker exec codenova-demo id
docker rm --force codenova-demo
```

The image build copies only `requirements.txt` and `app/` into the runtime image. The build context excludes Git metadata, local Claude settings, virtual environments, environment files, private-key files, tests, and documentation. Do not pass credentials as Docker build arguments or bake them into the image. Verify the final image configuration and app files:

```bash
docker image inspect codenova-devops-portfolio:latest --format '{{json .Config.Env}}'
docker run --rm --entrypoint sh codenova-devops-portfolio:latest -c 'id; find /app -maxdepth 3 -type f -print'
```

Optional read-only source mount for local development (the image's installed dependencies remain unchanged):

```bash
docker run --rm -p 8000:8000 \
  --mount "type=bind,source=$PWD/app,target=/app/app,readonly" \
  codenova-devops-portfolio:latest
```

Record a terminal screenshot showing the successful build, image size, `id` output, and `/health` response. The actual image size depends on the platform and dependency versions; record the measured output rather than quoting an estimate.
