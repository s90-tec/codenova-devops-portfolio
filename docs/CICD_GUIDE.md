# CI/CD Guide

The `ci-cd.yml` workflow runs sequentially:

1. Lint: Ruff checks source quality.
2. Test: pytest runs only after lint succeeds.
3. Build: Docker builds only after tests pass.
4. Deploy: on pushes to `main`, the workflow calls the Render deploy hook if configured.

## Configure deployment secret

1. Create a web service on Render using this GitHub repository and select Docker as the runtime.
2. Obtain the service's deploy hook URL from its Render settings.
3. In GitHub, open Settings → Secrets and variables → Actions → New repository secret.
4. Name it `RENDER_DEPLOY_HOOK_URL` and paste the URL as its value.
5. Never put the URL in source code or commit it.

If the secret is absent, the deploy step reports that deployment was skipped. Configure it to make deployment active.

## Failure and rollback
A failed lint, test, or build job prevents deployment because each downstream job depends on the previous one. For rollback, use the hosting provider's previous successful deployment or redeploy a known-good commit. Verify the live health endpoint after deployment.
