Student Record:

Create a student dictionary  for n students with the student name as key and their test mark assignment mark and lab mark as values. Do the following computations and display the result.
1.Identify the student with the  highest average score
2.Identify the student who as the highest Assignment marks
3.Identify the student with the Lowest lab marks
4.Identify the student with the lowest average score
Note:
If more than one student has the same score display all the student names
Sample input:
4
James 67 89 56
Lalith 89 45 45
Ram 89 89 89
Sita 70 70 70
Sample Output:
Ram
James Ram
Lalith
Lalith

For example:
Input	             Result
4                  Ram
James 67 89 56     James Ram
Lalith 89 45 45    Lalith
Ram 89 89 89       Lalith
Sita 70 70 70	

Program:

n=int(input())
d={}
for i in range(n):
    na=input().split()
    d[na[0]]=[int(na[1]),int(na[2]),int(na[3])]
    l=int(na[3])

h=0
for i in d:
    if h< sum(d[i]):
        h=sum(d[i])
        j=i
        h1=sum(d[i])
print(j)
h=0


for i in d:
    if(h<d[i][1]):
        h=d[i][1]
        j=i
for i in d:
    if(h==d[i][1]):
        print(i,end=" ")
l1=[]
k=[]
print()
for i in d:
    if(l>d[i][2]):
        l=d[i][2]
        j=i
for i in d:
    if(l==d[i][2]):
        l1.append(i)
for i in range(-1,-len(l1)-1,-1):
    print(l1[i],end=" ")
print()

for i in d:
    if h1> sum(d[i]):
        h1=sum(d[i])
        j=i
print(j)
