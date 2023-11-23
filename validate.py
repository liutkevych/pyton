import re

email = input("What's your e-mail? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|net|edu|pl)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")