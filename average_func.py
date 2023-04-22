# Gets 3 args and return the average value

def get_average(num1, num2, num3):
    # code block
    total = num1 + num2 + num3
    average = total/3
    return average


a = 10
b = 15
c = 17

result = get_average(a, b, c)

print("Average of", a, b, c, " is equal to: ", result)
