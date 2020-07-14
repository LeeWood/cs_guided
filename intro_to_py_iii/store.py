class Store: #name should be uppercase and match file name...best practice
    def __init__(self, name, categories): #our constructor
        #*attributes
        self.name = name #!the right hand side needs to match the parameter list!
        self.categories = categories
        # at this point...we have a *template* for the store...we still have to instantiate the object! 

    def __str__(self): #!We have to tell Python how to print this object out.
        #return f'{self.name} has {len(self.categories)} categories'
        output = self.name
        #1. category...
        #2. 2nd category...
        i = 1
        for cat in self.categories:
            output += f"\n{i}. {cat}"
            i += 1

        return output    

    def __repr__(self):
        return f'{self.name} has {len(self.categories)} categories'

from category import Category #these are in the same directory...so this is all we have to do!

#my_store = Store("Wags N Wiggles", ["animal care", "borks", "food", "toys for good bois"]) #we're making categories a list because it's multiples

#using the new Category class...
my_store = Store("Wags N Wiggles", [Category("animal care"), Category("borks"), Category("food"), Category("toys for good bois")])

print( my_store )
print( my_store.__repr__() ) #this is more for developers.

#add input parser
selection = int(input('Category Number:\n'))
print(f'You Selected {my_store.categories[selection]}')

#? What if we wanted category objects instead of category strings??? See the category.py file

