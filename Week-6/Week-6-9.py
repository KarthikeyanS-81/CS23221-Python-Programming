Merge List:

Write a Python program to Zip two given lists of lists.

Input:
m : row size
n: column size
list1 and list 2 :  Two lists
Output
Zipped List : List which combined both list1 and list2
Sample test case

Sample input
2
2
1 
3
5
7
2
4
6
8
Sample Output
[[1, 3, 2, 4], [5, 7, 6, 8]]

Program:

m=int(input())
n=int(input())
l1=[]
l2=[]
c=1
for i in range(0,m*n*2,2):
    a=int(input())
    b=int(input())
    if c%2!=0:
        l1.append(a)
        l1.append(b)
    else:
        l2.append(a)
        l2.append(b)
    c=c+1
l3=[]
l3.append(l1)
l3.append(l2)
print(l3)
