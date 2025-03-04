# Fabio Castro Morffi 2438078
import random
import sys
def tileLabels(n):
    lst = []
    for i in range(1, n**2):
        lst.append(f'{i} ' if i < 10 else f'{i}')
    lst.append('  ')
    return lst

#print(tileLabels(3))
def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def getNewPuzzle(n):
    new_labels = tileLabels(n)
    random.shuffle(new_labels)
    display_lst = []
    for i in range(0,len(new_labels),n):
        display_lst.append(new_labels[i:i+n])
    print(display_lst)
    return display_lst


def findEmptyTile(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '  ':
                print(f"{i}, {j}")
                return (i, j)
                
#print(findEmptyTile(getNewPuzzle(4)) )           

def validMoves_helper(lst,position):
    valid_move = []
    if position[1] +1 < len(lst):
        valid_move.append("D")
    if position[1] -1 >= 0:
        valid_move.append("A")
    if position[0] +1 < len(lst):
        valid_move.append("W")
    if position[0] -1 >= 0:
        valid_move.append("S")
    return valid_move

def nextMove(lst):
    position = findEmptyTile(lst)
    val_move = validMoves_helper(lst,position)#["W","S","A","D"] 
    move = ''
    while move not in val_move:
        print(f"\n                          ({"W" if "W" in val_move else ' '})")
        print(f"Enter WASD (or QUIT): ({"A" if "A" in val_move else ' '}) ({"S" if "S" in val_move else ' '}) ({"D" if "D" in val_move else ' '})")
        move = input("> ")
        if move == "QUIT":
            sys.exit()
    return move
#print(nextMove(getNewPuzzle(4)) )       
    



    


    








