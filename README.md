# Python-projects

##1. Tic-Tac-Toe

Tic-Tac-Toe is a game where 2 opponents try to make a series of 3 consecutive symbol (linear or diagonal) and the one who do it first wins.
In this project I created one Tic-Tac-Toe game using Python programming language. 

Working:

At first it initialize one table matrix of 3 X 3 size with '_' symbol everywhere showing that those areas are unoccupied. Then it ask user to enter the coordinates where they want to make their move.
For example '1 1' means you want to make move on very first line of matrix. There is one while loop which is set to true to check if the coordinates which user is entering is correct or not.
If the input is correct then it will break else it will again ask user to enter the coordinates.

After taking input it will call function win() to check if player win or not. If not then it will call function easy_bot() which will make his move (by using random function).
After bot move it will again check if that bot win or not. If yes then it will break from loop else it will continue.

win() checks the winner by seeing if there is any row with all same symbols. Means if there are all 3 values equal to player symbol then it will return true means he won else it will check condition 
column wise if there is any match or not else again it will check for diagonal case. If there is no match found then it will return False means no one win.

This whole loop will run 5 times (means 9 times indirectly) if no one will win then it will print 'Tie'.