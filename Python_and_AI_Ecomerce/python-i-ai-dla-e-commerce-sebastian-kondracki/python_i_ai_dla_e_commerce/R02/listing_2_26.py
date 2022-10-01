class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def short_name(self):
        return self.first_name[0] + self.last_name[0]


customer1 = Customer("Jan", "Nowak", "jan.nowak@mailinator.com")
customer2 = Customer("Anna", "Kowalska", "anna.kowalska@mailinator.com")
print(customer1.short_name())
print(customer2.short_name())
