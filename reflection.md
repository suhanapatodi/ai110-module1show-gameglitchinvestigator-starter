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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
