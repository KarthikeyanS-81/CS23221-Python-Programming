Unique Names:

In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were first entered. For example, if the user enters:

Input: 
first
second
first
third
second

then your program should display:

Output:
first
second
third

Program:

l=[]
while(True):
    a=input()
    if a!=" ":
        l.append(a)
    else:
        break
l=dict.fromkeys(l)
for i in l:
    print(i)
