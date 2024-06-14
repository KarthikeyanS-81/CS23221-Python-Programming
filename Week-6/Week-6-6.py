Intersection of array:

Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.
Input Format
The first line contains T, the number of test cases. Following T lines contain:
1.      Line 1 contains N1, followed by N1 integers of the first array
2.      Line 2 contains N2, followed by N2 integers of the second array
Output Format
The intersection of the arrays in a single line
Example
Input:
1
3 10 17 57
6 2 7 10 15 57 246
Output:
10 57
Input:
1
7 
1 
2 
3 
3 
4 
5 
6
2 
1 
6
Output:
1 6


For example:
Input	Result
1     10 57
3 
10 
17 
57
6 
2 
7 
10 
15
57 
246
	
1    1 6
7 
1 
2 
3 
3 
4 
5 
6
2 
1 
6

Program:

t=int(input())
l1=list()
while(t!=0):
    n1=int(input())
    l1=[]
    l2=[]
    for i in range(0,n1):
        a=int(input())
        l1.append(a)
    n2=int(input())
    for i in range(0,n2):
        a=int(input())
        l2.append(a)
    t=t-1
    c=set(l1)
    d=set(l2)
    e=list(c.intersection(d))
    e.sort()
    for i in e:
        print(i,end=' ')
    print('\n')
