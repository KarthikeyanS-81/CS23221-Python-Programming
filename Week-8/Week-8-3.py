Scramble Score:

In the game of Scrabble™, each letter has points associated with it. The total score of a word is the sum of the scores of its letters. More common letters are worth fewer points while less common letters are worth more points. 
Write a program that computes and displays the Scrabble™ score for a word. Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.
A Scrabble™ board includes some squares that multiply the value of a letter or the value of an entire word. We will ignore these squares in this exercise.
The points associated with each letter are shown below:
Points Letters
1 A, E, I, L, N, O, R, S, T and U
2 D and G
3 B, C, M and P
4 F, H, V, W and Y
5 K
8 J and X
10 Q and Z

Sample Input
REC
Sample Output
REC is worth 5 points.
For example:
Input	Result
REC	REC is worth 5 points.

Program:

def calculate_scrabble_score(word):
    # Dictionary mapping letters to points
    letter_points = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10
    }
    
    score = 0
    for letter in word:
        letter = letter.upper()
        score += letter_points.get(letter, 0)  # Add the points for each letter, defaulting to 0 if not found
    
    return score

word=input()
score = calculate_scrabble_score(word)
print(f"{word} is worth {score} points.")
