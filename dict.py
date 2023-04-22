# CRUD Functions on dicts

# not to do
# d = {1:True, "one":"ONE", "PI":3.14}

# Populate a dictionary
products = {1: "apples", 2: "bananas", 3: "watermelon", 4: "strawberry"}
print("1", products)

# Insert
products[4] = "oranges"
print("2", products)

# Update
products[1] = "melon"
print("3", products)

# Delete
del products[2]
print("4", products)

# Access a specific key:value pair
print(products[4])
print("5", products)
