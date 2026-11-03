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

The [public repository](https://github.com/s90-tec/codenova-devops-portfolio) includes `.gitignore`, `LICENSE`, CI workflows, and task guides. `main` is the default branch. The repository has two feature branches: `feature/add-about-endpoint` and `feature/greeting-encoded-name-test` (which adds coverage for URL-encoded greeting names). The [first pull request](https://github.com/s90-tec/codenova-devops-portfolio/pull/1) is merged and [PR #2](https://github.com/s90-tec/codenova-devops-portfolio/pull/2) is open for the about endpoint and DevOps workflow updates. [Create a pull request for the second branch](https://github.com/s90-tec/codenova-devops-portfolio/compare/main...feature/greeting-encoded-name-test?expand=1) to submit its independent test change.

Recorded workflow evidence:

- [PR #2 checks](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41649422929): lint, tests, and Docker image build passed for commit `8d4db054b5da515c32f3dc9e75ba64519c0bd327`; deploy is skipped for a pull request.
- [Automated Tests run](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41649423141): passed for that commit.
- The [earlier Actions failure](https://github.com/s90-tec/codenova-devops-portfolio/actions/runs/41644003291) caught the duplicate `about` declaration during Ruff linting; the duplicate was removed and subsequent checks passed.
- The PR currently has no independent reviews, and GitHub reports branch protection is disabled. A repository administrator must enable branch protection and a teammate/second account must review before those requirements can be marked complete.

Save genuine screenshots of the branch/PR, review, and passing Actions checks for submission. The current PR has no description; add a meaningful summary, test results, and deployment impact in its GitHub description before requesting review.

## Peer review simulation
For a solo project, use a second GitHub account or ask a teammate to review. Do not claim an independent review if one did not happen.
