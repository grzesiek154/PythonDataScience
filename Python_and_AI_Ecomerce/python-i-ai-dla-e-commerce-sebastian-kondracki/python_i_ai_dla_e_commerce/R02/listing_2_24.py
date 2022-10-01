class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

customer1 = Customer("Jan", "Nowak", "jan.nowak@mailinator.com")
customer2 = Customer("Anna", "Kowalska", "anna.kowalska@mailinator.com")

print(customer1)
print(customer2)