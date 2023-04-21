# list populate
ages = [37, 42, 22, 27]

# iterate the list
for index, age in enumerate(ages):
    print(f"ages[{index}] is {age}")

print("-------------")

# enhanced for
for age in ages:
    print(age)

# range - question
for index, i in enumerate(range(5), start=1):
    print(index, i)
