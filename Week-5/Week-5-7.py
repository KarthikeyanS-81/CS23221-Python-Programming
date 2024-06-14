Longest Word:

Write a python to read a sentence and print its longest word and its length
For example:
Input	                             Result
This is a sample text to test	     sample
                                   6
 
Program:

sen=input()
words=sen.split()
l=""
maxi=0
for word in words:
    if(len(word)>maxi):
        l=word
        maxi=len(word)
print(l,maxi,sep="\n")
