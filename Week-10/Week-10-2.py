Peak Element
Given an list, find peak element in it. A peak element is an element that is greater than its neighbors.
An element a[i] is a peak element if
A[i-1] <= A[i] >=a[i+1] for middle elements. [0<i<n-1]
A[i-1] <= A[i] for last element [i=n-1]
A[i]>=A[i+1] for first element [i=0]
Input Format:

The first line contains a single integer n , the length of A .
The second line contains n space-separated integers,A[i].

Output Format
Print peak numbers separated by space.

Sample Input
5
8 9 10 2 6
Sample Output
10 6

For example:
Input	      Result
4           12 8
12 3 6 8 

Program:

a=int(input())
lst1=[str(x) for x in input().split(" ")]
lst2=[]
lst=[]
g=0
for i in lst1:
    if i.isdigit():
        g=int(i)
        lst.append(g)
for i in range(0,a):
    if(i==0):
        if(lst[i]>=lst[i+1]):
            lst2.append(lst[i])
    elif(i>0 and i<a-2):
        if(lst[i]>=lst[i-1] and lst[i]>=lst[i+1]):
            lst2.append(lst[i])
    elif(i==a-1):
        if(lst[i]>=lst[i-1]):
            lst2.append(lst[i])
for i in lst2:
    print(i,end=" ")
