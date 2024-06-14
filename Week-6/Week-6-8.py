Strictly increasing:

Write a Python program to check if a given list is strictly increasing or not. Moreover, If removing only one element from the list results in a strictly increasing list, we still consider the list true
Input:
n : Number of elements
List1: List of values
Output
Print "True" if list is strictly increasing or decreasing else print "False"

Sample Test Case
Input
7
1
2
3
0
4
5
6
Output 
True

Program:

def check_increasing_or_decreasing(lst):
    increasing = True
    decreasing = True
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False
    return increasing or decreasing

def check_strictly_increasing_with_removal(lst):
    for i in range(len(lst)):
        temp_lst = lst[:i] + lst[i+1:]
        if check_increasing_or_decreasing(temp_lst):
            return True
    return False
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input())
if check_increasing_or_decreasing(lst) or check_strictly_increasing_with_removal(lst):
    print("True")
else:
    print("False")
