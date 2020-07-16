class Product:
    def __init__(self, name, description, price=1):
        self.name = name
        self.desctription = description
        self.price = price

    def __str__(self):
        return f'{self.name} costs ${self.price}.'