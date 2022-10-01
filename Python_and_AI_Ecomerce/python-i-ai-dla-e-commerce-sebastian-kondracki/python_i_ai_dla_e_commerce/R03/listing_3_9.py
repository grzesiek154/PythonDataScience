import re

text = "Wszystkie wnioski i reklamacje proszę kierować na emaile: biuro@mailinator.com reklamacje@mailinator.com lub (błędny adres) sebastian@mailinator"
pattern = r'[\w\.]+@[\w\.]+\.[a-z]{2,3}'
for match in re.finditer(pattern, text):
    print(match)