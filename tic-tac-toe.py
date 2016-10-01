'''------------------------------------------------------------------
Author: Shashank Sharma
Language: Python
Project name: Tic-Tac-Toe Game
------------------------------------------------------------------'''

from random import randint

def easy_bot(table): # Automatic Easy bot with no knowledge
    while True:
        a = randint(0, 2)
        b = randint(0, 2)
        if table[a][b] == '_':
            table[a][b] = 'O'
            return table
        else:
            continue
def check(player,table): # Checks table if someone is winning or not
    for i in range(3):
        if table[i].count(player)<=2:
            continue
        else:
            return True
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i] == player:
            return True
        else:
            continue
    for i in range(1, 4):
        if table[i-1][i-1] == player:
            continue
        else:
            if table[2][0] == table[1][1] == table[0][2] == player:
                continue
            else:
                return False
            return True
    return True
#---------------------------------------MAIN
table = []
for i in range(3):
    table.append(['_'] * 3)
for i in table:
    print '     '.join(i), '\n'
win = False
count = 0
for count in range(9):
    print 'Enter the coordinates (example 1,1)'
    while True:
        a,b = raw_input().split()
        a = int(a)
        b = int(b)
        if a > 3 or b > 3:
            print 'Try correct move'
            continue
        if table[a-1][b-1] == '_':
            table[a-1][b-1] = 'X'
            break
        else:
            print 'Someone already made that move'
            print 'Please Try again'
            continue
    win = check('X',table)
    if count == 5:
        print '-----------------------------------'
        print 'No one wins'
        print '-----------------------------------'
        break
    if win:
        print '-----------------------------------'
        print 'PLAYER WON'
        print '-----------------------------------'
        break
    table = easy_bot(table)
    win = check('O',table)
    if win:
        print '-----------------------------------'
        print 'BOT wins'
        print '-----------------------------------'
        break
    for i in table:
        print '    '.join(i), '\n'


print '\n \nThank you for playing'
print 'Have a look at the board \n'
for i in table:
    print '    '.join(i), '\n'
print '\n Bye'