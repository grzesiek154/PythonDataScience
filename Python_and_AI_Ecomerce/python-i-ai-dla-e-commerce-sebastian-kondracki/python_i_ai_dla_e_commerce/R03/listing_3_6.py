import re

input_text = "Sebastian"
pattern = "se"
match = re.search(pattern, input_text, flags=re.I)
print(match)