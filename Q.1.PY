import random
import string

while True:
    password = input("Enter password: ")
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Character checks
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1

    if score >= 3:
        print("Strong Password")
        break
    else:
        print("Weak Password")
        print("Suggested Password:",
              ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8)))