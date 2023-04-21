import math

name = "Alice"
age = 30

print("CF")
print("PI = ", math.pi)
print("My name is", name, "and i am", age, "years old.")
print("My name is " + name + " and i am " + str(age) + " years old.")

# Python 2 style
print("PI = %6.2f" % math.pi)
print("%s is %d years old." % (name, age))

# Python 3 style
print("age is {0:2d}", format(age))
print("PI is {0:.3f}".format(math.pi))
print("{0} is {1} years old.".format(name, age))
print("{0:*^10}{1:>20}".format(name, age))

# f-strings and variables interpolation
print(f"My name is {name} and i am {age} years old.")
print(f"{name:>20}, {age:<5}")
