Winner of Election:

Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.
Examples: 
Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem
 
Sample Input:
10
John
John
Johny
Jamie
Jamie
Johny
Jack
Johny
Johny
Jackie

Sample Output:
Johny
 
For example:
Input	  Result
10      Johny
John
John
Johny
Jamie
Jamie
Johny
Jack
Johny
Johny
Jackie

Program:

n=int(input())
d={}
for i in range(n):
    s=input()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
h=0
for i in d:
    if h<d[i]:
        h=d[i]
        j=i
print(j)
