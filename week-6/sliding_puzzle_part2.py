# Fabio Castro Morffi 2438078
import random
import sys

def tileLabels(n):
    board_lst = []
    for i in range(1, n**2):
        board_lst.append(f'{i} ' if i < 10 else f'{i}')
    board_lst.append('  ')
    return board_lst

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
    display_board_lst = []
    for i in range(0,len(new_labels),n):
        display_board_lst.append(new_labels[i:i+n])
    #print(display_board_lst)
    return display_board_lst


def findEmptyTile(board_lst):
    for i in range(len(board_lst)):
        for j in range(len(board_lst[i])):
            if board_lst[i][j] == '  ':
                #print(f"{i}, {j}")
                return (i, j)
                
#print(findEmptyTile(getNewPuzzle(4)) )           

def validMoves_helper(board_lst,position):
    valid_move = []
    if position[1] +1 < len(board_lst):
        valid_move.append("A")
    if position[1]  -1 >= 0:
        valid_move.append("D")
    if '  ' not in board_lst[-1]:
        valid_move.append("W")
    if  '  ' not in board_lst[0]:
        valid_move.append("S")
    return valid_move

def nextMove(board_lst):
    position = findEmptyTile(board_lst)
    val_move = validMoves_helper(board_lst,position)#["W","S","A","D"] 
    move = ''
    while move not in val_move:
        print(f"\n                          ({"W" if "W" in val_move else ' '})")
        print(f"Enter WASD (or QUIT): ({"A" if "A" in val_move else ' '}) ({"S" if "S" in val_move else ' '}) ({"D" if "D" in val_move else ' '})")
        move = input("> ")
        if move.upper() == "QUIT":
            sys.exit()
    return move
#print(nextMove(getNewPuzzle(4)) )       
lst = getNewPuzzle(4)
def makeMove(board_lst,move):
    position = findEmptyTile(board_lst)
    i = position[0]
    j = position[1]
    #print(board_lst)
    if move == "W":
        board_lst[i][j], board_lst[i+1][j] = board_lst[i+1][j], board_lst[i][j]    
    #qprint(board_lst)
    if move == "A":
        board_lst[i][j], board_lst[i][j+1] = board_lst[i][j+1], board_lst[i][j]
    if move == "S":
        board_lst[i][j], board_lst[i-1][j] = board_lst[i-1][j], board_lst[i][j]
    if move == "D":
        board_lst[i][j], board_lst[i][j-1] = board_lst[i][j-1], board_lst[i][j]

def main():
    print("Hello fellow Player:")
    print("Your objective in this game is to organize TILES \nsuch that the numbers " \
          "are in order from top to bottom left to right.") 
    print("What should the size of the puzzle be? (Either 3 or 4)")
    size = int(input("> "))
    board = getNewPuzzle(size)
    displayBoard(board)
    count_moves = 0
    while count_moves < (31 if size == 3 else 80):
        makeMove(board, nextMove(board))
        displayBoard(board)
        if size == 3 and board == [['1 ', '2 ', '3 '],['4 ','5 ','6 '], ['7 ','8 ', '  ']] \
            or size == 4 and board == [['1 ', '2 ', '3 ', '4 '], ['5 ','6 ','7 ','8 '], ['9 ','10','11','12'],['13','14','15','  ']]:
            print("Amazing you did it!")
            sys.exit()
        count_moves += 1
    print("Best of luck next time!")
#makeMove(lst, nextMove(lst))
main()


    


    








