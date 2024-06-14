Merge Two Sorted Arrays Without Duplication:

Output is a merged array without duplicates.
Input Format
N1 - no of elements in array 1
Array elements for array 1
N2 - no of elements in array 2
Array elements for array2
Output Format
Display the merged array
Sample Input 1
5
1 
2 
3 
6 
9
4
2 
4 
5 
10
Sample Output 1
1 2 3 4 5 6 9 10

Program:

n1=int(input())
l1=[]
for i in range(0,n1):
    a=int(input())
    l1.append(a)
n2=int(input())
l2=[]
for i in range(0,n2):
    a=int(input())
    l2.append(a)
l3=[]
l3.extend(l1)
l3.extend(l2)
a=list(set(l3))
a.sort()
for i in a:
    print(i,end=' ') n1=int(input())
l1=[]
for i in range(0,n1):
    a=int(input())
    l1.append(a)
n2=int(input())
l2=[]
for i in range(0,n2):
    a=int(input())
    l2.append(a)
l3=[]
l3.extend(l1)
l3.extend(l2)
a=list(set(l3))
a.sort()
for i in a:
    print(i,end=' ')
