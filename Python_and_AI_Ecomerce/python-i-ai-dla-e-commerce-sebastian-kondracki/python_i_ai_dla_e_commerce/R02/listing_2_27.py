import smtplib, ssl


class Customer:
    sender = "sebastian.kondracki@dobry-przykladowy-hosting.pl"
    sender_label = "SYSTEM E-COMMERCE"
    login = "sebastian.kondracki@dobry-przykladowy-hosting.pl"
    password = "5mde_SUPER_TAJNE_HASLO_SW"
    host = "serwer_smtp.dobry-przykladowy-hosting.pl"
    port = 587

    def __init__(
        self, name, phone, email, street, house_number, flat_number, city, zip_code
    ):
        self.name = name
        self.phone = phone
        self.email = email
        self.street = street
        self.house_number = house_number
        self.flat_number = flat_number
        self.city = city
        self.zip_code = zip_code

    def send_email(self, subject, txt):
        receivers = [self.email]
        message = (
            "From: "
            + self.sender_label
            + " <"
            + self.sender
            + ">\nTo: "
            + self.name
            + " <"
            + self.email
            + ">\nSubject: "
            + subject
            + "\n\n"
            + txt
        )

        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        connection = smtplib.SMTP(self.host, self.port)
        connection.ehlo()
        connection.starttls(context=context)
        connection.ehlo()
        connection.login(self.login, self.password)
        return connection.sendmail(self.sender, receivers, message.encode("utf-8"))


class Person(Customer):
    def __init__(
        self,
        first_name,
        last_name,
        phone,
        email,
        street,
        house_number,
        flat_number,
        city,
        zip_code,
    ):
        self.first_name = first_name
        self.last_name = last_name
        Customer.__init__(
            self,
            self.first_name + " " + self.last_name,
            phone,
            email,
            street,
            house_number,
            flat_number,
            city,
            zip_code,
        )

    def print_label(self):
        return (
            "Sz.P. "
            + self.first_name
            + " "
            + self.last_name
            + "\n"
            + self.street
            + " "
            + self.house_number
            + " "
            + self.flat_number
            + "\n"
            + self.zip_code
            + " "
            + self.city
            + "\n"
        )


class Company(Customer):
    def __init__(
        self,
        company_name,
        nip,
        phone,
        email,
        street,
        house_number,
        flat_number,
        city,
        zip_code,
    ):
        self.company_name = company_name
        self.nip = nip
        Customer.__init__(
            self,
            company_name,
            phone,
            email,
            street,
            house_number,
            flat_number,
            city,
            zip_code,
        )

    def print_label(self):
        return (
            self.company_name
            + "\n"
            + self.street
            + " "
            + self.house_number
            + " "
            + self.flat_number
            + "\n"
            + self.zip_code
            + " "
            + self.city
            + "\n"
        )


customer1 = Person(
    "Jan",
    "Nowak",
    "+48600111222",
    "jan.nowak@mailinator.com",
    "ul. Wielka",
    "12",
    "1A",
    "Wrocław",
    "32-231",
)

customer2 = Company(
    "Importex sp. z o.o.",
    "1112223344",
    "+48600333444",
    "sebastian.kondracki@gmail.com",
    "ul. Niska",
    "1",
    "",
    "Wrocław",
    "32-231",
)

print(customer1.print_label())
print(customer2.print_label())
print(customer2.send_email("Życzenia", "Zdrowych i Wesołych Świąt"))
