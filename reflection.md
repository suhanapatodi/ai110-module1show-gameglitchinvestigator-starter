# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game loaded a basic Streamlit interface with a text box for entering guesses, a submit button, and a score display. However, the hint logic was inverted, range validation was missing, and the game reset button did not reset the state properly.

- List at least two concrete bugs you noticed at the start  
  1. The high/low hint feedback was inverted (guessing higher than the secret number returned "Too Low").
  2. The "Start New Game" button does not reset or start a new game state when clicked.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| Guess `150` (Secret is `50`)| Show error that guess must be between 1 and 100| Accepts input and tells user to "go higher"| None|
| Guess `70` (Secret is `50`)| Show hint "go lower"| Shows hint "go higher"|None |
|Guess '30' (Secret is '50') | Shows hint "go higher"|Shows hint "go lower" | None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Gemini / AI coding assistant to help troubleshoot test errors, debug parameter ordering issues, and structure my code refactoring.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
**Suggestion:** The AI suggested using `python -m pytest` instead of running `pytest` directly to solve a `ModuleNotFoundError` where Python couldn't find `logic_utils.py`.
**Verification:** Running `python -m pytest` immediately resolved the import error and allowed `pytest` to collect the test suite files.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
**Suggestion:** During parameter order debugging, the AI suggested swapping the function signature order to `def check_guess(secret, guess)`.
**Why rejected/changed:** Changing the parameter order inverted the high/low comparison logic across the tests because `test_game_logic.py` called `check_guess(guess, secret)` expecting `guess` first. I kept the function signature as `check_guess(guess, secret)` and adjusted the internal comparison logic so that `guess > secret` properly mapped to `"Too High"`.
**Verification:** I saved all files (`Cmd + Option + S`) and ran `python -m pytest` in the terminal, confirming all 3 test cases passed in green.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
A bug was considered fixed when all unit tests in `tests/test_game_logic.py` passed with `pytest`, and the interactive Streamlit game behaved correctly without throwing errors or reporting inverted feedback.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
**Pytest:** I ran `python -m pytest` to test `test_winning_guess`, `test_guess_too_high`, and `test_guess_too_low`. The tests showed that `check_guess` was properly refactored out of `app.py` into `logic_utils.py` and returned the expected `(outcome, message)` tuple for all boundary cases.

- Did AI help you design or understand any tests? How?
Yes, the AI helped analyze the `AssertionError` tracebacks in the terminal output to pinpoint that `test_guess_too_high` was receiving `'Too Low'` due to inverted comparison logic, making it easy to fix the underlying issue.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time a user interacts with a widget in Streamlit, the entire Python script reruns from top to bottom. Session state acts as a persistent memory dictionary that holds onto variables like scores and secret numbers across those full script reruns. Without session state, the app would reset all variables to their default starting values after every single user click.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to keep separating core business logic into helper modules (`logic_utils.py`) so I can test functions with automated unit tests before connecting them to a user interface.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will carefully verify AI code suggestions against my existing function signatures and requirements before applying changes to avoid accidentally introducing parameter or logic conflicts.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI is an effective debugging partner for interpreting complex error traces, but developers must remain in control to evaluate and refine suggested solutions.