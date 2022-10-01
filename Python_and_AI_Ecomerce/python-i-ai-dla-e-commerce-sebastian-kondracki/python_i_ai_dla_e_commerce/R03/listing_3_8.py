import re

def is_mail(email):
    pattern = r'^[\w\.]+@[\w\.]+\.[a-z]{2,}$'
    if re.match(pattern, email, re.IGNORECASE):
        return True
    return False

print(is_mail("sebastian@@mailinator.com"))
print(is_mail("sebastian.kondracki@mailinator.com"))
print(is_mail("@mailinator.com"))
print(is_mail("sebastian@mailinator"))
print(is_mail("Sebastian@mailinator.STORE"))