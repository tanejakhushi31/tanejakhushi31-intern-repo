# Understanding Merge Conflicts

## What caused the conflict?
The conflict happened because I edited the same line of the file `notes.txt` in two different branches (`main` and `feature-branch`). Git could not automatically decide which version to keep, so it marked the file as conflicted.

## How did I resolve it?
I opened the conflicted file and saw the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). These showed me the two different versions. I manually chose the final content I wanted to keep, removed the conflict markers, and saved the file. Then I staged the file again and committed the resolution.

## What did I learn?
I learned that merge conflicts occur when changes overlap on the same part of a file. Resolving them requires human decision-making to pick or combine the correct changes. This process ensures that no important work is lost, and that the final version of the code is clear and consistent.
