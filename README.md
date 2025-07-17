Code Functionality of check-even-odd.py

#Check if a Number is Even or Odd

Step 1: Takes an input From User and Converts it into an Integer
number = int(input("Enter a number: "))

Step 2: Checks if the input number is even by dividing the number by 2
if number % 2 == 0:
    print(f"{number} is an even number.") #Prints this Statement if the number is divisible by 2
else:
    print(f"{number} is an odd number.") #prints this statement if the number is not divisible by 2

--------------------------------------------------------------------------------------------------------------------------

Code Functionality Of 1to50sum.py

#Sum of Integers from 1 to 50 using a loop

# Step 1: Initialize the sum
total = 0

# Step 2: Loop from 1 to 50
for i in range(1, 51):
    total += i  # Add each number to total

# Step 3: Display the result
print("The sum of numbers from 1 to 50 is:", total)

