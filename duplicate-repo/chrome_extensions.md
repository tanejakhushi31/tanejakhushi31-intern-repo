# chrome_extensions.md

## Which extensions did you install? Why?
1. **React Developer Tools** – To inspect React component trees, props, state, hooks, and check render timings via the Profiler. It’s the go-to for understanding component structure and debugging UI issues.
2. **Redux DevTools** – To view the Redux store, actions, diffs, time‑travel debug (jump between states), and export/import traces. Critical when tracking complex state bugs.
3. **JSON Viewer** (any reputable one, e.g., “JSON Viewer” or “JSON Formatter”) – To automatically pretty‑print JSON in the browser with collapsible nodes and syntax highlighting; hugely improves readability of API responses.
4. **Lighthouse** – To audit performance, accessibility, best practices, SEO, and PWA. Helps find render‑blocking issues, unused JS/CSS, and accessibility violations.

> Note: I installed these on **Google Chrome**, but they also work on Chromium-based browsers like Edge and Brave. React/Redux tools also expose panels in **Chrome DevTools** once installed.


### Initial checks / config
- **React Developer Tools**: Open DevTools → saw new **Components** and **Profiler** tabs. Verified React detection by loading a React app and confirming the flame icon next to the tab.
- **Redux DevTools**: Opened **DevTools → Redux** tab (or extension popup for legacy integrations). In app code, confirmed the store enhancer was detected (modern Redux Toolkit apps work out-of-the-box).
- **JSON Viewer**: Opened a raw JSON endpoint → confirmed it auto‑formatted with collapsible sections, line numbers, and copy button.
- **Lighthouse**: DevTools → **Lighthouse** panel. Set **Mode: Navigation**, **Device: Mobile**, throttling: *Simulated* (default).

## Short how‑tos (quick muscle memory)
- **Open DevTools**: `F12` or `Ctrl+Shift+I` (Windows/Linux), `Cmd+Opt+I` (macOS)
- **React Components**: DevTools → **Components** tab → select a node → inspect props/state; use the search box to find component names.
- **React Profiler**: DevTools → **Profiler** → **Start profiling** → interact → **Stop** to see commit phases and which components re-rendered.
- **Redux DevTools**:
  - **Action list**: inspect payloads and diffs
  - **Time travel**: click any action in the timeline to jump app state
  - **Trace**: enable stack traces in settings to see where actions originated
- **JSON Viewer**: Press **Collapse/Expand all** to get a structural overview, search for keys, and copy JSON fragments.
- **Lighthouse**: Run audits, then use **View Treemap** to find large bundles; check **Diagnostics** for render‑blocking resources; verify **Accessibility** contrasts and ARIA labels.

## Most useful things I learned today
- **React Profiler clarifies re‑renders**: Recording a short interaction showed which components re‑rendered and why, helping me spot unnecessary renders and props drilling.
- **Redux time‑travel is a superpower**: Being able to jump between past states and inspect diffs made it much easier to reproduce and isolate state bugs.
- **Lighthouse’s actionable tips**: The audit doesn’t just give a score—it links to concrete fixes (e.g., preloading key requests, reducing unused JS). Running on mobile emulation surfaces issues I wouldn’t see on desktop.
- **A good JSON viewer reduces cognitive load**: Pretty‑printing and folding large payloads saved time compared to reading raw responses in a single line.

## Next steps for me
- Add **React Developer Tools** “Highlight updates when components render” to catch extra renders.
- Configure **Redux DevTools** to persist sessions and export traces for bug reports.
- Use **Lighthouse CI** in the pipeline later to track performance regressions over time.
