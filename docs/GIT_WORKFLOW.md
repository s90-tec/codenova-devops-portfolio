# Git and GitHub Collaboration Workflow

## Branch naming
- `main`: stable branch
- `feature/<short-description>`: new functionality
- `fix/<short-description>`: bug fixes
- `docs/<short-description>`: documentation changes

## Commit convention
Use Conventional Commits:
- `feat: add greeting endpoint`
- `fix: correct health response`
- `test: add API endpoint tests`
- `docs: explain local setup`
- `ci: add automated test workflow`

## Pull request process
1. Create a feature branch from `main`.
2. Make a focused change and commit it.
3. Push the branch to GitHub.
4. Open a pull request into `main`.
5. Review the diff and leave a review comment (self-review is acceptable for a solo demonstration).
6. Ensure the Actions checks pass.
7. Merge the pull request and delete the feature branch.

Example commands:

```bash
git switch main
git pull --ff-only
git switch -c feature/describe-change
# edit, test, and review the diff
git add app tests
git commit -m "feat: describe change"
git push -u origin feature/describe-change
```

Open a pull request from the pushed branch into `main` using GitHub. Include the purpose, implementation summary, test results, and any deployment impact in the description. Only merge after required checks and a real review are complete.

## Repository setup and evidence

The [public repository](https://github.com/s90-tec/codenova-devops-portfolio) includes `.gitignore`, `LICENSE`, CI workflows, and task guides. `main` is the default branch. As of the current audit, PRs #1 through #6 are merged: #1/#2 add the about endpoint and CI/Docker/Render configuration, #3 adds encoded-name test coverage, and #4-#6 document the deployment strategy and merge-conflict exercise.

The merged PRs demonstrate feature branching, Conventional Commits, multiple commits, and PR-based merges. The feature branches still exist on the remote; delete them from GitHub after confirming they are no longer needed if branch cleanup is part of the submission rubric. Independent peer approval is not evidenced by the self-review comments.

Recorded workflow evidence:

- [Automated Tests on latest main](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41674968349): passed.
- [CI-CD on latest main](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41674968264): lint, tests, and Docker build passed; deploy failed because `RENDER_DEPLOY_HOOK_URL` is not configured. The log did not print a secret value.
- [PR #6 checks](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41674933652): lint, tests, and Docker build passed; deploy was correctly skipped for a pull request.

Save genuine screenshots of the merged PRs and passing Actions checks for submission. Screenshots are not currently checked into the repository.

## Peer review simulation

### Maintainer self-review record

This is a documented self-review simulation, not an independent peer approval.

- Scope: endpoint implementation, endpoint tests, both GitHub Actions workflows, Docker build context, and task documentation on PR #2.
- Review check: confirmed one `/about` route remains and added endpoint and unknown-route assertions.
- Review check: ran pytest (5 passed), Ruff, YAML parsing, Docker image build, container `/health`, and non-root UID verification.
- Finding resolved: duplicate `about` declarations caused Ruff `F811`; the extra declaration was removed before the successful checks.
- Finding resolved: Python cache files were initially included in the Docker context; nested cache exclusions were added and the image rebuilt/rechecked.
- Outstanding: obtain independent reviewer evidence on a future PR; the merged PRs do not document an independent approval.
