# Merge Conflict Demonstration

Perform this exercise in a disposable local clone or a temporary practice repository. Do not create the conflicting commits on the project's real `main` branch.

1. In a temporary directory, initialize a small Git repository and add a file:

   ```bash
   mkdir merge-conflict-demo
   cd merge-conflict-demo
   git init -b main
   printf 'Welcome to CodeNova\n' > welcome.txt
   git add welcome.txt
   git commit -m "chore: add initial welcome"
   ```

2. Create and commit a feature branch change to `welcome.txt`, then switch back to `main` and commit a different edit to the same line:

   ```bash
   git switch -c feature/change-welcome
   printf 'Welcome to the feature branch\n' > welcome.txt
   git commit -am "feat: change feature welcome"
   git switch main
   printf 'Welcome to main\n' > welcome.txt
   git commit -am "docs: change main welcome"
   ```

3. Merge the branch to produce a real conflict:

   ```bash
   git merge feature/change-welcome
   ```

   Git should report a conflict in `welcome.txt`. Resolve it to the desired final wording in an editor. Remove all conflict markers:
   `<<<<<<<`, `=======`, and `>>>>>>>`.

4. Verify and finish:

   ```bash
   git add welcome.txt
   git commit -m "fix: resolve welcome message merge conflict"
   git status
   git grep -n -E '^(<<<<<<<|=======|>>>>>>>)' || true
   ```

The practice repository is disposable; retain it only if you need it for a live demonstration. Capture genuine screenshots of Git's conflict output and the resolved commit. Do not add a fabricated conflict to the application source or claim this demonstration has been run unless you performed it.
