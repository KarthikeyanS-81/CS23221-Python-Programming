EXCEPTION HANDLING:

Write a Python program that performs division and modulo operations on two numbers provided by the user. Handle division by zero and non-numeric inputs.
Input Format:
Two lines of input, each containing a number.
Output Format:
Print the result of division and modulo operation, or an error message if an exception occurs.
For example:
Input	Result
10  Division result: 5.0
2   Modulo result: 0

7   Division result: 2.3333333333333335
0   Modulo result: 1

8   Error: Cannot divide or modulo by zero.
0
  
Program:
  
try:
    a=input()
    b=input()
    c=int(a)/int(b)
    d=int(a)%int(b)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except:
    print("Error: Non-numeric input provided.")
else:
    print("Division result:",c)
    print("Modulo result:",d)
