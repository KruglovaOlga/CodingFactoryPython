# CRUD in lists

grades = [1, 4, 5, 5, 10, 7]
print("Grades: ", grades)

# append
grades.append(8)
print("Grades after append: ", grades)

# update
grades[1] = 5
print("Grades after update: ", grades)

# delete
grades.remove(1)
print("Grades after remove: ", grades)

# search with value
if 10 in grades:
    print("Wow!")

# index()
if 1 in grades:
    position_to_update = grades.index(1)
    grades[position_to_update] = 9
# position_to_update = grades.index(10)

# if position_to_update != -1:
#     grades[position_to_update] = 9

print("Final grades list: ", grades)
