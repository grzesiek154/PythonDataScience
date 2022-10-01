import re

text = "Sebastian Kondracki, 54-233 Wrocław, sebastian@mailinator.com Jan Kowalski, 46-200 Kluczbork, jan@mailinator.com"
pattern_email = r'[\w\.]+@[\w\.]+\.[a-z]{2,3}'
pattern_zip_code = r'[0-9]{2}-[0-9]{3}'

for match in re.finditer(pattern_email, text):
    print(match)
    
for match in re.finditer(pattern_zip_code, text):
    print(match)