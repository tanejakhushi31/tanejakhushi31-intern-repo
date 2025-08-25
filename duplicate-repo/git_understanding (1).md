## What is the difference between staging and committing?
- **Working directory**: Your edited files on disk.
- **Staging area (index)**: A holding area where you pick exactly which changes will be part of the next commit. (In VS Code: *Stage Changes*)
- **Commit (HEAD)**: A permanent snapshot of everything currently staged, saved with a message, author, and timestamp.

**Staging** = selecting changes to include in the next snapshot.  
**Committing** = creating the actual snapshot from whatever is staged.

## Why does Git separate these two steps?
- **Selective commits**: Include only the parts you want (e.g., bug fix now; refactor later).
- **Clean history**: Craft focused, readable commits instead of dumping everything.
- **Review before record**: Double‑check diffs while they’re staged.
- **Partial file control**: Stage specific hunks/lines for precise commits.
- **Safer workflow**: Keep work‑in‑progress uncommitted while you validate tests/tools on staged changes.

## When would you stage changes without committing?
- You’re preparing a **focused commit**, but still editing other files.
- You want teammates to **review staged diffs** before you finalize.
- You’re **splitting a large change** into smaller logical commits.
- You need to **run hooks/tests** on the exact staged set before committing.
- You’re mid‑task and want to **park ready bits** without finalizing history yet.


## Hands‑on in VS Code
1) **Make a change** in any tracked file (e.g., `README.md`). Save.
2) **Stage only that file**: Open **Source Control** (`Ctrl+Shift+G`) → under **Changes**, click **+** next to the file (or right‑click → **Stage Changes**). It moves to **Staged Changes**.
3) **Check status**: In VS Code you’ll see it under **Staged Changes**. Terminal equivalent:
   ```bash
   git status
   # Expect: "Changes to be committed:" lists the file
   ```
4) **Unstage**: Click the **–** next to the file (or right‑click → **Unstage**). Terminal equivalents:
   ```bash
   git reset HEAD <file>
   # or
   git restore --staged <file>
   ```
5) **Commit**: Stage it again → type a message in the Source Control input (e.g., `Explain staging vs committing`) → press **Ctrl+Enter** or click the **✓ Commit** icon.
6) **Push to GitHub**: Click the **↑** icon in the status bar (or Source Control **…** → **Push**). If it’s a new branch, choose **Publish Branch**.
