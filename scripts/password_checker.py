# Family Password Checker (Examples Only)
# This checks password strength for EXAMPLES, not real passwords.

print("Family Password Checker (examples only)")
print("Type 'quit' to exit.\n")

while True:
    pw = input("Enter an EXAMPLE password to test: ")
    if pw.lower() in {"quit", "exit"}:
        print("Bye! Remember: long passphrases are your superpower.")
        break

    score = 0
    tips = []

    # Length
    if len(pw) >= 12:
        score += 2
    else:
        tips.append("Make it longer (aim for 12+ characters).")

    # Mix
    if any(c.isupper() for c in pw):
        score += 1
    else:
        tips.append("Add at least one CAPITAL letter.")
    if any(c.islower() for c in pw):
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")
    if any(c.isdigit() for c in pw):
        score += 1
    else:
        tips.append("Add at least one number.")
    if any(not c.isalnum() for c in pw):
        score += 1
    else:
        tips.append("Add at least one symbol (! ? _ #).")

    if "password" in pw.lower() or "1234" in pw:
        tips.append("Avoid common words or numbers like 'password' or '1234'.")

    if score >= 5:
        verdict = "Great 💪 — strong example!"
    elif score >= 3:
        verdict = "Good 🙂 — could be stronger."
    else:
        verdict = "Weak ⚠️ — needs work."

    print(f"\nScore: {score}/6 — {verdict}")
    if tips:
        print("Try this:")
        for t in tips:
            print(" -", t)
    else:
        print("Nice! Keep using long, unique passphrases.")
    print()
