Bubble Sort:

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. You read an list of numbers. You need to arrange the elements in ascending order and print the result. The sorting should be done using bubble sort.

Input Format: The first line reads the number of elements in the array. The second line reads the array elements one by one.

Output Format: The output should be a sorted list.

For example:
Input	          Result
6
3 4 8 7 1 2	    1 2 3 4 7 8

5 
4 5 2 3 1	      1 2 3 4 5

Program:

n=int(input())
k=[int(x) for x in input().split()]
k.sort()
for i in k:
    print(i,end=' ')
