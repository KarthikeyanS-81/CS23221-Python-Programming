Sort Dictionary by Values Summation:

Give a dictionary with value lists, sort the keys by summation of values in value list.
 Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}
Output : {‘Gfg’: 17, ‘best’: 18}
Explanation : Sorted by sum, and replaced.
 Input : test_dict = {‘Gfg’ : [8,8], ‘best’ : [5,5]}
Output : {‘best’: 10, ‘Gfg’: 16}
Explanation : Sorted by sum, and replaced.
 Sample Input:
2
Gfg 6 7 4
Best 7 6 5
Sample Output
Gfg 17
Best 18
 
For example:
Input	       Result
2            Gfg 17
Gfg 6 7 4    Best 18
Best 7 6 5

Program:
n = int(input())
d = {}
for i in range(n):
    s = input().split()
    d[s[0]] = list(map(int, s[1:]))
d1 = {k: sum(v) for k, v in d.items()}
sorted_d = dict(sorted(d1.items(), key=lambda x: x[1]))
for k, v in sorted_d.items():
    print(k, v)
