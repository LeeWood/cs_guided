# Agenda
#     -Review unique characteristics of Python syntax
#     -Apply UPER to solve a code challenge in Python
#     -Build a Python class, complete with:
#         __init__()
#         __str__()
#         __repr__()
#     -Differentiate between class and instance methods/variables


# 1. Create & manipulate lists
# create an empty list
emptylist = []
# create a list with some numbers
listnum = [1, 2, 3, 4]
# add an element to p
listnum.append(5)
# print all values in each list
print(listnum)
# OR 
for i in listnum:
    print(i)
#OR
for(i, item) in enumerate(listnum):
    print(f'Element {i} is {item}')
#* I really need to get down and dirty in the Python docs...
    
# ...How are lists different from tuples? Sets? Dictionaries?
#* yah yah the mutabilty, repeatability, etc is all different between the different datastructures


# 2. Use list comprehensions to perform the same operation on all list elements
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create a new list containing the squares of all values in `numbers`
squares = [num ** 2 for num in numbers]
#OR
'''
squares = []
for num in numbers:
    squares.append(num ** 2)
'''
print("squares:", squares)



# Create a new list containing only the even values of `numbers`
evens = [num for num in numbers if num % 2 == 0]


names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
# Create a new list containing only the names that start with `s` so that they are properly capitalized (regardless of how the name originally appears) 


# 3. Dictionary exercise from module I project





# 4. Pass by value vs. reference
# Define a doubling function that take in integers...
def mult2(x):
  pass

# And a doubling function that takes in a LIST of integers
def mult2_list(l):
  pass

# Try out our functions -
# What will happen to the original arguments after we  
# call the functions? Will they be modified? Or not?
y = mult2(12)
print(y)

l = [3,7,13]
mult2_list(l)

for i in l:
  print(i)


# 5. Review the 4 steps of UPER and apply 
# to the following mini-challenges:

# Return the "centered" average of an array of ints, which we'll 
# say is the mean average of the values, except ignoring the 
# largest and smallest values in the array. 
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3


# 6. Questions from last week's project


# 7. Build Python classes `store` and `category`, complete with:
#         __init__()
#         __str__()
#         __repr__()


# 8. Go over the Adventure Game starter code


# Next time...
# -Understand the convention for "private" methods and vars in Python
# -Explan LEGB rule for variable scope in Python
# -Differentiate between class and instance methods/variables
# -Demonstrate inheritance relationships with method overriding and use of super()
# -Identify association in class design