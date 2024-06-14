Check Product of Digits:

Write a code to check whether product of digits at even places is divisible by sum of digits at odd place of a positive integer.
Input Format:
Take an input integer from stdin.

Output Format:
Print TRUE or FALSE.

Example Input:
1256

Output:
TRUE

Example Input:
1595

Output:
FALSE

For example:

Test	                      Result
print(productDigits(1256))	True
print(productDigits(1595))	False


Program:

def productDigits(n):
    a=n
    temp=[]
    list1=[]
    list2=[]
    rem=0
    while a!=0:
        rem=a%10
        temp.append(rem)
        a=a//10
    for i in range(len(temp)):
        if(i+1)%2==0:
            list1.append(temp[i])
        else:
            list2.append(temp[i])
    pro=1
    sum=0
    for i in list1:
        sum+=i
    for i in list2:
        pro*=i
    if pro%sum==0:
        return True
    else:
        return False
