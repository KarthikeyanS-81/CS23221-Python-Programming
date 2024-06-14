Remove Palindrome Words:

String should contain only the words are not palindrome.

Sample Input 1
Malayalam is my mother tongue

Sample Output 1
is my mother tongue

Program:

s=input()
words=s.split()
x=''
for word in words:
    word=word.lower()
    if (word!=word[::-1]):
        print(word,end=" ")
