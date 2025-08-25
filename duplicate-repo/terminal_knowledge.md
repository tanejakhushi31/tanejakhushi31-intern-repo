# terminal_knowledge.md

## Which terminal client did you choose? Why?
I chose **Windows Terminal + PowerShell** on Windows. Windows Terminal lets me keep multiple shells (PowerShell, Command Prompt, Git Bash) in tabs/panes with fast rendering, good Unicode support, and easy JSON-based settings. PowerShell gives me powerful objects/pipelines, rich tab completion, and nice modules like `PSReadLine`.

## What customizations did you make?
- **Prompt & theme**: Installed **Oh My Posh** for a clean, informational prompt (git branch + status, exit codes, clock). I used the `paradox` theme to keep things minimal.
- **Autocomplete & history**: Enabled `PSReadLine` with prediction (history + AI-like suggestions) and `Tab` to accept.
- **Aliases** (in my PowerShell profile):
  - `alias gs = git status`
  - `alias ga = git add`
  - `alias gc = git commit`
  - `alias gp = git push`
  - `alias ll = Get-ChildItem -Force`
  - `alias gco = git checkout`
- **Quality‑of‑life**:
  - Set Windows Terminal to open in my projects folder.
  - Added a **Git Bash** profile as an optional tab for POSIX-style tools.

## Setup commands I ran (PowerShell)
> Tip: run PowerShell as Administrator when using `winget`.

```powershell
# 1) Install Windows Terminal (if not already installed)
winget install --id Microsoft.WindowsTerminal -e

# 2) Ensure PowerShell is up to date (optional)
winget install --id Microsoft.PowerShell -e

# 3) Prompt theming
winget install JanDeDobbeleer.OhMyPosh -s winget

# 4) PSReadLine (ships with PS 7+, but this refreshes)
Install-Module PSReadLine -Scope CurrentUser -Force

# 5) Create/Open my PowerShell profile
if (!(Test-Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
notepad $PROFILE
```

Then I added this to my **PowerShell profile** (the file opened by the last command):
```powershell
# ----- Prompt/theme -----
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\paradox.omp.json" | Invoke-Expression

# ----- PSReadLine quality-of-life -----
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineKeyHandler -Key Tab -Function AcceptSuggestion
Set-PSReadLineOption -EditMode Windows

# ----- Aliases -----
Set-Alias gs 'git status'
Set-Alias ga 'git add'
Set-Alias gc 'git commit'
Set-Alias gp 'git push'
Set-Alias gco 'git checkout'
function ll { Get-ChildItem -Force @args }
```

## Most useful command I learned today
`Get-Help` and its alias `help` were the most useful. Example:  
```powershell
Get-Help Get-ChildItem -Online
```
This opens the official docs for a command in the browser. It helped me quickly discover parameters and examples without leaving the terminal.

**Honourable mentions**:
- `gcm <name>` (`Get-Command`) to discover which command will run.
- `code .` to open the current folder in VS Code.
- `git status` to see repo state at a glance.
- `wt -p "PowerShell" -p "Git Bash"` to open multiple profiles in Windows Terminal.

## Notes / reflections
- The combo of Windows Terminal + PowerShell gives me a fast, modern shell with great UX.  
- `Oh My Posh` made my prompt informative (especially for Git work), which reduced context‑switching.  
- Custom aliases speed up repetitive git flows.  
- Knowing `Get-Help` well is a superpower; it shortens the learning curve for any new command.
