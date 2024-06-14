EXCEPTION HANDLING :

Write a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.
Input Format: A single line input representing the user's age.
Output Format: Print a message based on the age or an error if the input is invalid.

For example:
Input	  Result
twenty  Error: Please enter a valid age.

25      You are 25 years old.

-1      Error: Please enter a valid age.

Program:

try:
    a=input()
    if int(a)>=0:
        print("You are",a,"years old.")
    else:
        print("Error: Please enter a valid age.")
except:
    print("Error: Please enter a valid age.")
