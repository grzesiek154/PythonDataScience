new_customer = set()
returning_customer = set()
vip_customer = set()

new_customer.add("Pieluchy")
new_customer.add("Szampony i odżywki")
new_customer.add("Herbaty i napary")
new_customer.add("Kawy")
new_customer.add("Mleko")

returning_customer.add("Maślanki")
returning_customer.add("Mleko")
returning_customer.add("Napoje alkoholowe")
returning_customer.add("Soki")
returning_customer.add("Wody")
returning_customer.add("Wędliny")
returning_customer.add("Kawy")
returning_customer.add("Jogurty")
returning_customer.add("Herbaty i napary")
returning_customer.add("Masła i margaryny")
returning_customer.add("Szampony i odżywki")
returning_customer.add("Serki ziarniste")
returning_customer.add("Sery")
returning_customer.add("Śmietanki do kawy")
returning_customer.add("Śmietany")

vip_customer.add("Napoje alkoholowe")
vip_customer.add("Szampony i odżywki")
vip_customer.add("Świeże i mrożone owoce morza")

all_category = new_customer | returning_customer | vip_customer
print("Suma wszystkich zbiorów kategorii", all_category)
intersection_category = new_customer & returning_customer & vip_customer
print("Część wspólna wszystkich zbiorów kategorii",
intersection_category)
only_returning_category = returning_customer - vip_customer - new_customer
print("Kategorie pojawiające się tylko u powracających klientów",
only_returning_category)
only_new_category = new_customer - returning_customer - vip_customer
print("Kategorie pojawiające się tylko u nowych klientów",
only_new_category)
symmetric_difference_category = new_customer ^ returning_customer ^ vip_customer
print("Różnica symetryczna kategorii", symmetric_difference_category)