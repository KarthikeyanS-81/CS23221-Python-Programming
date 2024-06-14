MODULES-USING DICTIONARY:

Rose manages a personal library with a diverse collection of books. To streamline her library management, she needs a program that can categorize books based on their genres, making it easier to find and organize her collection.

Problem Statement:
Develop a Python program that reads a series of book titles and their corresponding genres from user input, categorizes the books by genre using a dictionary, and outputs the list of books under each genre in a formatted manner.

Input Format:

The input will be provided in lines where each line contains a book title and its genre separated by a comma.
Input terminates with a blank line.
Output Format:

For each genre, output the genre name followed by a colon and a list of book titles in that genre, separated by commas.
Constraints:

Book titles and genres are strings.
Book titles can vary in length but will not exceed 100 characters.
Genres will not exceed 50 characters.
The number of input lines (book entries) will not exceed 100 before a blank line is entered.



For example:
Input	                                           Result
Introduction to Programming, Programming         Programming: Introduction to Programming
Advanced Calculus, Mathematics                   Mathematics: Advanced Calculus

Fictional Reality, Fiction                       Fiction: Fictional Reality, Another World
Another World, Fiction	

Program:

d = {}
while True:
    try:
        book = input().split(',')
        if len(book) < 2:
            continue
        book_name = book[0].strip()
        category = book[1].strip()
        if category in d:
            d[category].append(book_name)
        else:
            d[category] = [book_name]
    except EOFError:
        break

for k, v in d.items():
    print(f"{k}: ", end='')
    print(', '.join(v))
