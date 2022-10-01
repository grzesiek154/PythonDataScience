import re

input_text = "abc 123 def"
pattern = "[0-9]"
for match in re.findall(pattern,input_text):
    print(match)