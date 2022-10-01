import re

input_text = "Sebastian"
pattern = "se"
pattern_with_flag = "(?i)se"
match1 = re.search(pattern, input_text)
match2 = re.search(pattern, input_text, re.I)

match3 = re.search(pattern, input_text, re.IGNORECASE)
match4 = re.search(pattern_with_flag, input_text)
print(match1)
print(match2)
print(match3)
print(match4)