# Populating a tuple

ages = 30, 40, 25, 27

print(type(ages))

# simple for
for index, age in enumerate(ages):
    print(f"{index} : {age}")

# enhanced for
for age in ages:
    print(age)
