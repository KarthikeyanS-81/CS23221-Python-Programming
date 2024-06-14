Uncommon words:

A sentence is a string of single-space separated words where each word consists only of lowercase letters.A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
Note:
Use dictionary to solve the problem
For example:
Input	                 Result
this apple is sweet    sweet sour
this apple is sour

Program:

s1 = input().split()
s2 = input().split()
d = {}
for i in s1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in s2:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] == 1:
        print(i, end=" ")
