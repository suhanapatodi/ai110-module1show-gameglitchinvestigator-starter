def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Hard":
        return 1, 50
    return 1, 100  # Default / Normal


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored out of app.py and added range validation
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).
    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Corrected inverted logic (guess > secret should say Go LOWER!)
    if guess == secret:
        return ("Win", "Congratulations! You guessed the correct number!")
    elif guess > secret:
        return ("Too High", "Your guess is too high! Try again.")
    else:
        return ("Too Low", "Your guess is too low! Try again.")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points
    return current_score - 5
