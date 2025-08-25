# ai_tools.md

## Which AI tools did you try?
I used **ChatGPT** for:
- Generating small code snippets (Python and JavaScript).
- Debugging a simple bug.
- Explaining a new concept I’m learning.

> Rationale: I wanted a fast, general-purpose assistant that can switch between “explain like I’m 5” and “show me the exact code,” and that works outside the editor for broader Q&A and planning.


## What I did (experiments)

### 1) Generate code snippets
**Task:** “Write a Python function that flattens a nested list of arbitrary depth.”  
**Result (excerpt):**
```python
def flatten(xs):
    for x in xs:
        if isinstance(x, (list, tuple)):
            yield from flatten(x)
        else:
            yield x
# list(flatten([1,[2,[3,4]],5])) -> [1,2,3,4,5]
```
**Usefulness:** High for quickly getting a correct baseline and test idea. I still reviewed edge cases (e.g., generators vs. lists, handling non-iterables).

### 2) Debug a simple problem
**Bug:** Off‑by‑one error in this JS loop (last item skipped):
```js
for (let i = 0; i < arr.length - 1; i++) {
  total += arr[i];
}
```
**Prompt to ChatGPT:** “Why is my sum missing the last element?”  
**Suggestion:** Use `i < arr.length` or adjust termination condition.  
**Outcome:** Fixed quickly, plus got a one‑liner using `reduce`:
```js
const total = arr.reduce((a, b) => a + b, 0);
```

### 3) Explain a new concept
**Topic:** Event loop & microtasks vs macrotasks (JS).  
**What I asked:** “Explain with a minimal example and step order.”  
**Takeaway:** Clear ordering explanation with a timeline showing `Promise.then` (microtask) running before `setTimeout` (macrotask), plus a tiny demo I could paste into DevTools.


## What worked well
- **Speed to first draft:** Useful for boilerplate, patterns, and exploring multiple approaches (e.g., recursion vs. stack).
- **Debug reasoning:** Good at spotting common pitfalls and proposing simpler alternatives.
- **Teaching mode:** Solid conceptual explanations with runnable mini‑examples and analogies.

## What didn’t work
- **Occasional hallucinations:** Can invent APIs or omit edge cases; code compiles but fails in specifics.
- **Context limits:** Without my actual project code, advice can be generic.
- **Security/perf nuance:** Needs careful review for input validation, error handling, and performance characteristics.


## When AI is most useful for coding
- **Rapid prototyping:** Generate scaffolds/tests to move faster, then refine.
- **Pattern recall:** Reminding best practices (e.g., debounce vs throttle, binary search template).
- **Bug triage:** Getting hypotheses and quick repro steps.
- **Learning & docs:** Digesting new APIs, comparing trade‑offs, and creating minimal examples.
- **Explaining code:** Summarizing unfamiliar files or functions.

**When to be cautious**
- Critical paths (auth, crypto, concurrency) → verify against official docs.
- Large refactors → pair with tests and code review.
- Framework/config specifics → confirm versions and compatibility.


## Practical prompting tips I used
- **Give constraints:** “ES2020 only,” “no external deps,” “O(n log n) or better.”
- **Provide failing case:** Paste input/output and error to focus the answer.
- **Ask for tests:** “Include 3 unit tests, highlight edge cases.”
- **Request rationale:** “Explain why you chose this approach in 2 lines.”
