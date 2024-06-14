Automorphic number or not:

An automorphic number is a number whose square ends with the number itself. For example, 5 is an automorphic number because 5*5 =25. The last digit is 5 which same as the given number. 

If the number is not valid, it should display “Invalid input”.
If it is an automorphic number display “Automorphic” else display “Not Automorphic”.

Input Format:
Take a Integer from Stdin 
Output Format: 
Print Automorphic if given number is Automorphic number, otherwise Not Automorphic 
Example input: 5 Output: Automorphic Example input: 25 Output: Automorphic Example input: 7 Output: Not Automorphic
For example:
Test				             Result
print(automorphic(5))	   Automorphic
                                                       
Program:
                                                       
def automorphic(n):
    if(n<0):
        return "Invalid input"
    square = n  * n
    n_s=str(n)
    s_s=str(square)
    if s_s.endswith(n_s):
        return "Automorphic"
    else:
        return "Not Automorphic"
