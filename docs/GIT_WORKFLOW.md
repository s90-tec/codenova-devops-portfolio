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

The repository includes `.gitignore`, `LICENSE`, CI workflows, and task guides. Confirm the repository is public in GitHub Settings and that `main` is the default branch. Configure branch protection and required status checks in GitHub Settings; those settings are server-side and are not represented by these files. Save genuine screenshots of the branch/PR, review, and passing Actions checks for submission.

## Peer review simulation
For a solo project, use a second GitHub account or ask a teammate to review. Do not claim an independent review if one did not happen.
