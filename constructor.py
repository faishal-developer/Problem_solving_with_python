class Phone:
    manufactured="China"

    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price
    

phone = Phone('faishal',"symphony",58755)
# class attributes
print(Phone.manufactured)

# isinstance attributes
print(phone.brand)