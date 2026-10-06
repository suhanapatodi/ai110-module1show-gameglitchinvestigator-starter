# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---
## Challenge 1: Advanced Edge-Case Testing

### Prompts Used
- "Identify three potential edge-case inputs for input parsing/game logic (like empty strings, out-of-bounds integers, and float strings) and write pytest cases for parse_guess."

### Edge Cases Chosen & Rationales
1. **Empty / Non-numeric Strings (`""`, `"abc"`):** Chosen because raw user text inputs from UI text fields can often be empty or contain non-digit characters, which can cause unhandled ValueError crashes if not parsed safely.
2. **Out-of-Bounds Integers (`0`, `150`):** Chosen because guesses outside the designated difficulty range (e.g. 1 to 100) waste player attempts and need clean error validation messages.
3. **Decimal Strings (`"50.0"`):** Chosen because users or Streamlit numeric inputs might pass string floats, which `int()` fails on directly unless converted through `float()` first.


## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
