user_input = int(input("Please enter a positive integer:"))
print("The factors of", user_input, "are:")
for factor in range(1,user_input):
    if user_input % factor == 0:
        print(factor)