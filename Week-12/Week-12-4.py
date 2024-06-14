MODULE-POWER OF FOUR:

Given an integer n, print true if it is a power of four. Otherwise, print false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
For example:
Input	Result
16	  True
5	    False

Program:

a=int(input())
c=0
for i in range(a):
    if a==2**i:
        c+=1
if c==1:
    print("True")
else:
    print("False")
