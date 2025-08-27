## Why is pushing directly to main problematic?

Pushing directly to main can introduce bugs or incomplete features into
the codebase, which may break the application for everyone. Since main
is considered the "production-ready" branch, unexpected changes can
reduce stability and make it harder for teams to trust the code.

## How do branches help with reviewing code?

Branches allow developers to isolate new features or bug fixes without
affecting the main branch. Team members can create Pull Requests from
their branch, making it easier for others to review changes, suggest
improvements, and ensure code quality before merging into main.

## What happens if two people edit the same file on different branches?

If two people edit the same file in different branches, Git will try to
merge them automatically. However, if the edits overlap (e.g., same line
of code), a **merge conflict** occurs. The team must manually resolve
the conflict by deciding which changes to keep or how to combine them.
This process ensures collaboration without losing anyone's work.
