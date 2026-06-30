"""
Week 2 Final Project — Password Strength Checker
=================================================
Pure Python — no external dependencies, no API keys, no internet.
This is the "Advanced" tier of the Week 2 assignment.

Concepts demonstrated:
- Functions, conditionals, loops
- String methods + regex (`re` module)
- Lists, sets, dictionaries
- Returning multiple values

Run:
    python week2_password_checker.py
"""

import re

# Top 10 most-cracked passwords of all time. If your password is here,
# attackers crack it in milliseconds.
COMMON_WEAK = {
    "password", "12345678", "qwerty", "letmein", "iloveyou",
    "admin", "welcome", "monkey", "dragon", "football",
    "nepal", "kathmandu", "123456789", "password1", "abc123",
}

# Sequential patterns attackers try first
SEQUENCES = [
    "0123", "1234", "2345", "3456", "4567", "5678", "6789",
    "abcd", "bcde", "qwerty", "asdf", "zxcv",
]


def check_password(password: str) -> tuple[int, str, list[str]]:
    """
    Score a password from 0-100 and return (score, label, feedback).

    Scoring breakdown:
      Length 8-11 chars  → +15
      Length 12+ chars   → +30
      Each char class    → +15  (lowercase, uppercase, digit, special)
      Penalties for common words, repeats, sequences
    """
    feedback = []
    score = 0

    # ---- Length ----
    length = len(password)
    if length < 8:
        feedback.append(f"❌ Too short ({length} chars). Use at least 8.")
    elif length >= 16:
        score += 35
        feedback.append("✅ Excellent length (16+)")
    elif length >= 12:
        score += 30
        feedback.append("✅ Great length (12+)")
    else:
        score += 15
        feedback.append("👌 OK length, but 12+ is much stronger")

    # ---- Character variety ----
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-\[\]/\\+=]", password))

    variety = sum([has_lower, has_upper, has_digit, has_special])
    score += variety * 15

    if not has_lower:
        feedback.append("❌ Add a lowercase letter")
    if not has_upper:
        feedback.append("❌ Add an uppercase letter")
    if not has_digit:
        feedback.append("❌ Add a digit")
    if not has_special:
        feedback.append("❌ Add a symbol (!@#$ etc.)")
    if variety == 4:
        feedback.append("✅ Excellent character mix")

    # ---- Common-password check ----
    if password.lower() in COMMON_WEAK:
        score = min(score, 10)
        feedback.append("🚨 This is one of the most-cracked passwords. Change it.")

    # ---- Repeated chars (aaa, 111) ----
    if re.search(r"(.)\1{2,}", password):
        score -= 10
        feedback.append("⚠️  Avoid repeated characters (aaa, 111)")

    # ---- Sequential patterns ----
    lowered = password.lower()
    for seq in SEQUENCES:
        if seq in lowered:
            score -= 10
            feedback.append(f"⚠️  Avoid sequence '{seq}'")
            break

    # ---- Clamp + label ----
    score = max(0, min(100, score))
    if score >= 80:
        label = "💪 STRONG"
    elif score >= 50:
        label = "👌 MEDIUM"
    elif score >= 25:
        label = "⚠️  WEAK"
    else:
        label = "🚨 VERY WEAK"

    return score, label, feedback


def progress_bar(score: int, width: int = 20) -> str:
    """Render a unicode progress bar."""
    filled = int(score / 100 * width)
    return "█" * filled + "░" * (width - filled)


def main():
    print("=" * 50)
    print("🔐  PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print()

    # Demo a few first
    demos = ["hello", "Hello1", "Hello1!", "MyD0g$Name!Rex2024"]
    for pwd in demos:
        score, label, feedback = check_password(pwd)
        print(f"Password: {pwd!r}")
        print(f"  [{progress_bar(score)}]  {score}/100  {label}")
        for line in feedback[:3]:  # show first 3 only
            print(f"    {line}")
        print()

    print("-" * 50)
    print("Try your own (typing won't be hidden — just for practice):")
    print("-" * 50)

    while True:
        pwd = input("\nEnter password (or 'quit'): ")
        if pwd.lower() == "quit":
            break
        if not pwd:
            continue
        score, label, feedback = check_password(pwd)
        print(f"  [{progress_bar(score)}]  {score}/100  {label}")
        for line in feedback:
            print(f"    {line}")


if __name__ == "__main__":
    main()
