Check pair with difference k:

Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Input Format
1.      First line is number of test cases T. Following T lines contain:
2.      N, followed by N integers of the array
3.      The non-negative integer k
Output format
Print 1 if such a pair exists and 0 if it doesn’t.
Input
1
3 
1 
3 
5
4
Output:
1
Input
1
3 
1 
3 
5
99
Output
0


For example:
Input	Result
1     1
3 
1 
3 
5
4	

1     0
3 
1 
3 
5
99	

Program:

t=int(input())
for i in range(0,t):
    n=int(input())
    l=[]
    for j in range(0,n):
        a=int(input())
        l.append(a)
    p=int(input())
    for k in range(0,n):
        c=0
        for m in range(i+1,n):
            if l[m]-l[k]==p:
                c=1
                print('1')
                break
        if c==1:
            break
    if c==0:
        print('0')
