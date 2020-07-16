from product import Product

class Crate(Product): #importing the parent class. Inheritance
    def __init__(self, name, description, price, size, material):
        super().__init__(name, description, price) #pulling in the attr. from the parent class
        self.size = size
        self.material = material
