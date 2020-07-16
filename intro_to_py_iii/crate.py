from product import Product

class Crate(Product): #importing the parent class. Inheritance
    def __init__(self, name, description, price, size, material):
        super().__init__(name, description, price) #pulling in the attr. from the parent class
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f' and is made out of {self.material}'
        # ^^^ here we're using the string methon from the parent class vs overwriting it like in the return statement below...Reusability is a plus of Python and we're taking advantage of that. It's easier to maintain and update. 

        #return f'{self.name} costs ${self.price} and is made of {self.material}.'

c = Crate("cool crate", "it's the BEST", 10, "medium", "METAL")

print(super(Crate, c).__str__()) #this is using super to override the __str__ that is defined in this class and using the parent method. 
print(c)
