EXCEPTION HANDLING:

Develop a Python program that safely performs division between two numbers provided by the user. Handle exceptions like division by zero and non-numeric inputs.
Input Format: Two lines of input, each containing a number.
Output Format: Print the result of the division or an error message if an exception occurs.

For example:
Input	Result
10    5.0
2

10    Error: Cannot divide or modulo by zero.
0
ten   Error: Non-numeric input provided.
5

Program:

try:
    a=input()
    b=input()
    c=float(a)/float(b)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except:
    print("Error: Non-numeric input provided.")
else:
    print(c)
