# Dict traverse

products = {1: "apples", 2: "bananas", 3: "watermelon", 4: "strawberry"}

# Traverse the keys of dict with keys()
for key in products.keys():
    print(key)

# Traverse the keys-value pairs of dict with keys()
for value in products.values():
    print(value)

# Traverse the keys - values pairs of dict with items()
for key, value in products.items():
    print(key, ":", value)
