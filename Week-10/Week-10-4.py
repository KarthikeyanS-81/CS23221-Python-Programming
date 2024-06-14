Sum of Two numbers:

An list contains N numbers and you want to determine whether two of the numbers sum to a given number K. For example, if the input is 8, 4, 1, 6 and K is 10, the answer is yes (4 and 6). A number may be used twice.
Input Format
The first line contains a single integer n , the length of list
The second line contains n space-separated integers, list[i].
The third line contains integer k.
Output Format
Print Yes or No.
Sample Input
7
0 1 2 4 6 5 3 
1 
Sample Output
Yes

For example:
Input	              Result
5                   Yes
8 9 12 15 3
11	

6                    No
2 9 21 32 43 43 1
4

Program:

n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
flag=0
if len(a)!=n:
    print("No")
    flag=1
for i in a:
    for j in a:
        if i+j==k and flag==0:
            flag=1
            print("Yes")
            break
if flag==0:
    print("No")
