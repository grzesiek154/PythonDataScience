import hashlib

customer1 = "Jan, Nowak, 62102715242"
print("MD5:", customer1, hashlib.md5(customer1.encode("utf-8")).hexdigest())
print("SHA-2", customer1, hashlib.sha256(customer1.encode("utf-8")).hexdigest())
customer2 = "Anna, Kowalska, 59092276792"
print("MD5:", customer2, hashlib.md5(customer2.encode("utf-8")).hexdigest())
print("SHA-2", customer2, hashlib.sha256(customer2.encode("utf-8")).hexdigest())