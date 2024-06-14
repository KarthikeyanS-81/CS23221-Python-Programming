EXCEPTION HANDLING :

To find whether a digit lies in the specified range(1-100). Handling exceptions for invalid inputs and out-of-range numbers .
Input Format:
User inputs a number.
Output Format:
Confirm the input or print an error message if it's invalid or out of range.
For example:
Input	Result
1	    Valid input.
101	  Error: Number out of allowed range
rec	  Error: invalid literal for int()

Program:

try:
    a=input()
    if(int(a)>0 and int(a)<101):
        print("Valid input.")
    else:
        print("Error: Number out of allowed range")
except:
    print("Error: invalid literal for int()")
