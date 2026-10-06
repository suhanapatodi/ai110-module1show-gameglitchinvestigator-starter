# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose:**
  The Game Glitch Investigator is an interactive Streamlit-based number guessing game. Players select a difficulty level (which sets the valid guessing range) and attempt to guess a randomly generated secret number. The game provides real-time feedback after each guess (indicating whether the guess is too high, too low, or correct) and tracks player scores based on performance and attempt counts.

**Bugs Found:**
  1. **Inverted Feedback Logic:** The comparison logic in `check_guess` was inverted, returning "Too High" when a guess was lower than the secret number and vice-versa.
  2. **Unimplemented Function / Refactoring Needed:** The core game logic `check_guess` in `logic_utils.py` raised a `NotImplementedError` and needed to be refactored out of `app.py`.
  3. **Module Import Errors in Testing:** Running standard `pytest` commands threw `ModuleNotFoundError: No module named 'logic_utils'` because the root directory was not included in Python's search path.

**Fixes Applied:**
  1. Refactored `check_guess` into `logic_utils.py`, replacing the `NotImplementedError` with functional comparison logic.
  2. Corrected the conditional logic in `check_guess(guess, secret)` so that `guess > secret` properly yields `"Too High"` and `guess < secret` yields `"Too Low"`.
  3. Utilized `python -m pytest` to execute unit tests within the active virtual environment, ensuring proper module resolution.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "Normal" difficulty (Number range: 1–100) and starts a new game.
2. User enters a initial guess of `50`.
3. Game evaluates the guess using `logic_utils.check_guess()` and displays `"Too Low! Try again."`
4. The score updates based on the attempt count.
5. User enters a higher guess of `75`.
6. Game returns `"Too High! Try again."`
7. User enters `62`.
8. Game returns `"Win: Congratulations! You guessed the correct number!"`
9. Final score is calculated, displayed, and recorded in the game session.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
========================== test session starts ==========================
platform darwin -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/suhanapatodi/Documents/GitHub/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 6 items                                                       

tests/test_game_logic.py ......                                   [100%]

=========================== 6 passed in 0.03s ===========================
(.venv) suhanapatodi@Mac ai110-module1show-gameglitchinvestigator-starter

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
