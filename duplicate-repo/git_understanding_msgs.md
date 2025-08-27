# Commit Message Styles & Reflections

As part of this exercise, I created three commits with different commit message styles:
1. **Vague:** `fixed stuff`
2. **Overly detailed:** A multi‑line message that included every single changed line explanation, environment info, and unrelated notes.
3. **Well‑structured:** `feat: add input validation to login form` with a short subject line and optional descriptive body.

---

## What makes a good commit message?
- **Concise subject line** (~50 characters) summarising *what* the commit does, not *how*.
- Use **imperative mood** (e.g., "Add validation" not "Added validation") — it reads well in logs and matches auto‑generated messages (e.g., from `git merge`).
- Provide a body (wrapped at 72 chars) *when context matters*: explaining *why* the change was needed, trade‑offs made, or links to tickets/issues.
- Consistency — following a convention like Conventional Commits (`feat:`, `fix:`, `docs:`, etc.) or project guidelines.

## How does a clear commit message help in team collaboration?
- Makes code review easier: reviewers instantly know the intent before diving into the diff.
- Helps future developers (including myself) understand *why* a change happened months later.
- Improves tooling: structured messages can feed into automated changelogs, release notes, and semantic versioning.
- Reduces misunderstandings — especially in multi‑developer projects where context can get lost.

## How can poor commit messages cause issues later?
- **Vague messages** ("update", "fixed stuff") force everyone to read the diff to guess the purpose.
- **Overly detailed messages** clutter the log and bury the important "why" in noise.
- Harder to track down bugs: `git blame` or `git log` become less useful if messages don’t explain intent.
- Missed automation opportunities: inconsistent styles break changelog generators or release pipelines.