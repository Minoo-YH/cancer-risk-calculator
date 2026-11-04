
def calculate_demo_score(age, smoking, family_history):
    """Return a fictional educational score."""
    score = 0

    if age >= 50:
        score += 30
    elif age >= 35:
        score += 15

    if smoking == "current":
        score += 25
    elif smoking == "former":
        score += 10

    if family_history:
        score += 20

    return min(score, 100)

