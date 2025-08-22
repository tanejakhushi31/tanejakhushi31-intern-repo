# Git Knowledge – Reflections

## Have you used Git before? If so, in what context?
Yes. I used Git for coursework at uni. I practised the full flow: creating branches, making commits, opening pull requests, resolving a merge conflict, and pushing to GitHub. I worked in both a local test repository and a GitHub-backed repository.

## Which Git client (if any) did you choose? Why?
I used **GitHub Desktop** alongside **VS Code** and the **Git Bash** terminal.
- **GitHub Desktop**: great for seeing the file diff, commit history, and a clear “Changes → Summary → Commit → Push” flow. Conflict resolution is easier to understand visually.
- **Terminal (Git Bash / VS Code Terminal)**: faster for specific commands (e.g., `git status`, `git add`, `git commit`, `git push`, creating branches). Helpful when following step-by-step instructions or fixing edge cases.
Using both gave me confidence: GUI for visibility, terminal for precision.

## What was the most interesting thing you learned about Git today?
How **merge conflicts** are represented and resolved. I learned what the conflict markers mean:
```
<<<<<<< HEAD        # my current branch’s version
=======             # separator
>>>>>>> feature-branch  # the incoming branch’s version
```
To resolve, I decide on the final content, remove the markers, then stage and commit. I also noticed how Git reports state, like “Your branch is ahead of 'origin/main' by N commits,” which means I need to push to sync with GitHub. Finally, I saw how untracked files appear and how to either add them or ignore them via `.gitignore`.
