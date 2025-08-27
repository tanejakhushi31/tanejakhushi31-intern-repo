# Git Commands
## `git checkout main -- <file>`
**What it does:** Replaces the working copy of `<file>` on your current branch with the version from `main` (no branch switch; other files untouched).  
**When to use:** Undo a bad edit to one file, or pull a known‑good version from `main` without merging the whole branch. Great for quick, surgical rollbacks.  
**What surprised me:** It only works if the file exists in `main`’s history; otherwise Git errors. It overwrites the file in place—stash first if you might want to keep local edits.

---

## `git cherry-pick <commit>`
**What it does:** Replays a single commit’s changes onto the current branch, creating a new commit (new SHA).  
**When to use:** Hotfixes and backports—promote one fix to `main` or a release branch without bringing the whole feature.  
**What surprised me:** Conflicts can occur like merges; you must resolve and `--continue`. Repeated cherry‑picking the same change across branches can clutter history if not planned.

---

## `git log`
**What it does:** Shows commit history; with flags it becomes a powerful investigation tool.  
**When to use:** Trace when/why a change happened, prep release notes, visualise branches before merges. Try `--oneline --graph --decorate --all` or `-p -n 1` for diffs.  
**What surprised me:** The graph view dramatically improves mental mapping of branches and cherry‑picks. Filtering by file/author makes huge histories manageable.

---

## `git blame <file>`
**What it does:** Shows which commit/author last modified each line and when.  
**When to use:** Debugging and code archaeology—find the context/owner of a line before refactors or fixes. Pair with `git show <SHA>` for intent.  
**What surprised me:** `-w` ignores whitespace‑only changes (less noise with formatters). Blame tells “who last touched it,” not “why”—the commit message and diff provide that story.
