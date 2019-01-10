'''Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
'''

#attempt
'''
from typing import List

def checkio(game: List[str]) -> str:
    for i in range(3):
        if game[i][0] == game[i][1] and game[i][1] == game[i][2] and game[i][0]!= ".":
            return game[i][0]
        if game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[0][i]!= ".":    
            return game[0][i]
    
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] != '.':
            return game[0][0]
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] != '.':
            return game[0][2]
    
    return "D"
    
    
    

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    print (checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Os wins")
    assert checkio([
        ".XX",
        "OXO",
        "OOO"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "XXX"]) == "X", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
'''

print(i in range(5))