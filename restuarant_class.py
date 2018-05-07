class Restuarant:
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type

    def open_restuarant(self):
        print("The restuarant is open")
    def describe_restuarant(self):
        self.open_restuarant()


restuarant = Restuarant("Jones Fried Chicken", "Lamb over rice")
print(restuarant.restuarant_name)
print(restuarant.cuisine_type)
restuarant.describe_restuarant()
