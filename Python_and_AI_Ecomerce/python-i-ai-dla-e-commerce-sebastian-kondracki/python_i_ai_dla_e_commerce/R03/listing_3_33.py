views = ['audi ', 'skoda', 'mazda', 'toyota']
brands = (brand.upper() for brand in views)
for brand in brands:
    print(brand)