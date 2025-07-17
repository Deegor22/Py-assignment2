#Takes an number from User as an Integer.
num = int(input("Enter a number: "))
print()
#Checks If the Number is Divided by 2 or not if yes then prints the 1st statemet if not then prints the else statement.
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")