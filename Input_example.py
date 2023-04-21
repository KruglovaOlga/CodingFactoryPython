# String input() example
s = input("Give me your name: ")

# simple for
for i in range(len(s)):
    print(s[i], end=" ")
print()

# enhanced for
for char in s:
    print(char, end="")
