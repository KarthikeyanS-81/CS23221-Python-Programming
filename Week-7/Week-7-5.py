Check Pair:

Given a tuple and a positive integer k, the task is to find the count of distinct pairs in the tuple whose sum is equal to K.
Examples:
Input: t = (5, 6, 5, 7, 7, 8 ), K = 13 
Output: 2 
Explanation: 
Pairs with sum K( = 13) are  {(5, 8), (6, 7), (6, 7)}. 
Therefore, distinct pairs with sum K( = 13) are { (5, 8), (6, 7) }. 
Therefore, the required output is 2.

For example:
Input	      Result
1,2,1,2,5   1 
3	
  
1,2         0
0	

Program:

def count_distinct_pairs(t, K):
    distinct_pairs = set()
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] + t[j] == K:
                distinct_pairs.add((min(t[i], t[j]), max(t[i], t[j])))
    return len(distinct_pairs)
t_input = input()
t = tuple(map(int, t_input.split(',')))
K = int(input())
print(count_distinct_pairs(t, K))
