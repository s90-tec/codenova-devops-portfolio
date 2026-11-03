# CI/CD Guide

The `ci-cd.yml` workflow runs sequentially:

1. Lint: Ruff checks source quality.
2. Test: pytest runs only after lint succeeds.
3. Build: Docker builds only after tests pass.
4. Deploy: only on a push to `main`, the workflow calls the Render deploy hook. Pull requests run through the Docker build but never deploy. A manual `workflow_dispatch` run stops after the image build.

## Configure deployment secret

1. Create and configure a web service on Render using this GitHub repository and select Docker as the runtime.
2. Obtain the service's deploy hook URL from its Render settings.
3. In GitHub, open Settings → Secrets and variables → Actions → New repository secret.
4. Name it `RENDER_DEPLOY_HOOK_URL` and paste the URL as its value.
5. Never put the URL in source code or commit it.

The deployment step runs only after lint, tests, and the Docker image build pass. It fails clearly if the secret is absent or the deploy hook request fails. Configure the Render service and repository secret before relying on deployment. This workflow builds but does not publish an image to a registry; Render builds the repository itself.

## Verify a deployment

After a successful `main` push with the secret configured, check the GitHub Actions run and the Render deployment status, then open `https://<your-service-host>/health` and confirm it returns `{"status":"healthy"}`. Replace the placeholder host with the URL assigned by Render. Do not report a live deployment until this check succeeds.

## Failure and rollback
A failed lint, test, or build job prevents deployment because each downstream job depends on the previous one. A missing secret, network error, or non-successful deploy-hook response also fails the deploy job. Review the failing Actions step and Render service events, correct the root cause, and rerun the workflow.

For rollback, use Render's previous successful deployment or redeploy a known-good commit from the Render dashboard. If deployments are managed from GitHub, revert the bad change in a new commit and push it through the same pipeline. Verify `/health` after rollback. Never force-push or rewrite shared deployment history as a rollback.

## Test failure demonstration

The pipeline uses normal pytest exit codes: any failed assertion makes the test step and workflow fail. To capture a controlled failure without editing project tests or committing a failing change, run this in the activated virtual environment:

```bash
scratch_dir="$(mktemp -d)"
printf 'def test_deliberate_failure():\n    assert 1 == 2\n' > "$scratch_dir/test_failure_demo.py"
if PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider -q "$scratch_dir/test_failure_demo.py"; then
  failure_status=0
else
  failure_status=$?
fi
rm -f "$scratch_dir/test_failure_demo.py"
rmdir "$scratch_dir"
if [ "$failure_status" -ne 1 ]; then
  echo "Expected pytest exit code 1, received $failure_status"
  exit 1
fi
```

The output should show one failed assertion, while the script verifies pytest returned exit code 1 and removes only its own scratch file and directory. Then run `python -m pytest -v` and `python -m ruff check .` to demonstrate the clean project suite. Do not commit the intentionally failing test. A GitHub Actions failure/success screenshot requires running the corresponding workflow on GitHub.

For CI evidence, [Automated Tests run #5](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41644003291) is a real failed run, but it failed in Ruff on the duplicate `about` function, not in pytest. The later [Automated Tests run](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41651407483) and [CI-CD run](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41651407399) passed lint, tests, and image build for commit `4e3417630d04db3a2f7a7677906104cfbbc4808c`. The deploy job was skipped on the PR, as designed.

## Manual configuration that cannot be committed

- Add `RENDER_DEPLOY_HOOK_URL` under repository Settings → Secrets and variables → Actions.
- Protect `main` under Settings → Branches / Rulesets: require pull requests and require the `Automated Tests` and `CI-CD Pipeline` lint, test, and build checks after confirming their exact names on a pull request run. The deploy job is limited to pushes to `main`.
- A repository administrator or a second GitHub account must perform an independent review; do not describe self-review as peer review.
- Set up the Render service and confirm its assigned public URL and `/health` response before claiming a live deployment.

GitHub currently reports `main` is unprotected; branch rules and required checks must be enabled in repository settings by an administrator. The current pull request has no independent review yet.
