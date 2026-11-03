# Merge Conflict Demonstration

Perform this exercise on a separate practice branch or after pushing the initial project.

1. Create `feature/change-welcome-message` and change the welcome message in `app/main.py`.
2. Commit the change.
3. On `main`, change the same line to a different message and commit.
4. Merge the feature branch into `main`:

   ```bash
   git switch main
   git merge feature/change-welcome-message
   ```

5. Git should report a conflict in `app/main.py`.
6. Open the file, choose the intended final message, and remove all conflict markers:
   `<<<<<<<`, `=======`, and `>>>>>>>`.
7. Verify and finish:

   ```bash
   git add app/main.py
   git commit -m "fix: resolve welcome message merge conflict"
   git status
   ```

8. Confirm no conflict markers remain:

   ```bash
   grep -R -n -E '^(<<<<<<<|=======|>>>>>>>)' app tests || true
   ```

Record screenshots of the conflict and the successful resolution.
