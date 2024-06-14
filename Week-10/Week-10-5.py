Frequency of Elements:

To find the frequency of numbers in a list and display in sorted order.
Constraints: 
1<=n, arr[i]<=100 
Input: 
1 68 79 4 90 68 1 4 5 
output:
1 2
4 2
5 1
68 2
79 1 
90 1

For example:
Input	         Result
4 3 5 3 4 5	   3 2
               4 2
               5 2
	
Program:

lst5=[int(x) for x in input().split(" ")]
lst=sorted(list(set(lst5)))
c=0
for i in lst:
    c=0
    for j in lst5:
        if(i==j):
            c=c+1
    print("%d %d"%(i,c))
