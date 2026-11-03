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

## Peer review simulation
For a solo project, use a second GitHub account or ask a teammate to review. Do not claim an independent review if one did not happen.
