EXCEPTION HANDLING:

Develop a Python program that safely calculates the square root of a number provided by the user. Handle exceptions for negative inputs and non-numeric inputs.
Input Format:
User inputs a number.
Output Format:
Print the square root of the number or an error message if an exception occurs.
For example:
Input	Result
16	  The square root of 16.0 is 4.00
-4	  Error: Cannot calculate the square root of a negative number.
rec	  Error: could not convert string to float

Program:

import math
try:
    n=input()
    n=float(n)
    if n < 0:
        print("Error: Cannot calculate the square root of a negative number.")
    else:
        r= math.sqrt(n)
        print("The square root of {} is {:.2f}".format(n, r))
        
except ValueError:
    print("Error: could not convert string to float")
