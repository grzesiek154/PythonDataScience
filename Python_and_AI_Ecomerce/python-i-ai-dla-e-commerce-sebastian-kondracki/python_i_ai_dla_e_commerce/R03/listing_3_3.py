import re

phrases = ["kura", "plew", "kra", "zlew", "kira", "kąt"]
pattern = "k.*ra"
for phrase in phrases:
    for match in re.finditer(pattern, phrase):
        print(match)