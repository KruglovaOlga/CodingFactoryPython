# set example 02
# add(), remove()

# define a set
s = {5, 10, 10, 5, "Coding", 3.14, True, "Factory"}
print(s)
print(len(s))

# add some items
s.add(True)
print("1. Set after add: ", s)

s.add(100)
print("2. set after add: ", s)

s.remove(True)
print(" set after remove 'True': ", s)

# check with membership operator: in
print("Check if 10 exists: ", 10 in s)
