Christmas Discount:

An e-commerce company plans to give their customers a special discount for Christmas.
They are planning to offer a flat discount. The discount value is calculated as the sum of all the prime digits in the total bill amount.
Write an python code to find the discount value for the given total bill amount.
Constraints
1 <= orderValue< 10e100000
Input
The input consists of an integer orderValue, representing the total bill amount.
Output
Print an integer representing the discount value for the given total bill amount.
Example Input
578
Output
12
For example:
Test	                         Result
print(christmasDiscount(578))	 12

Program:
  
def is_prime_digit(digit):
    return digit in [2,3,5,7]
def christmasDiscount(n):
    s=discount=0
    prime_digitis=[2,3,5,7]
    for digit in str(n):
        digit=int(digit)
        if is_prime_digit(digit):
            discount+=digit
    return discount
