#Erica Bournival 2435250
import random
import sys

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

def tileLabels(n):
    if n <= 2:
        print('Invalid input')
        sys.exit()
    lst = []
    for i in range(1,n**2):
        lst.append(i)        
    lst.append('  ')
    return lst

def getNewPuzzle(n):
    sub_lst = tileLabels(n)
    random.shuffle(sub_lst)
    grouped = []

    for i in range(0, len(sub_lst), n):
        sub = sub_lst[i: i+n]
        grouped.append(sub)
    

    for row in range(len(grouped)):
        for col in range(len(grouped[row])):
            if grouped[row][col] == '  ':
                pass
            elif len(str(grouped[row][col])) == 1:
                grouped[row][col] = f'{grouped[row][col]} '
                
    return grouped
    
# ^ Finished everything above in class ^
            
def findEmptyTile(grouped):
    loc = None
    for row in range(len(grouped)):
        for col in range(len(grouped[row])):
            if grouped[row][col] == '  ':
                loc = (row, col)
                return loc

    return loc


def nextMove(grouped):
    n = len(grouped[0])
    while True:
        displayBoard(grouped)
        loc = findEmptyTile(grouped)
        W, A, S, D = '(W)', '(A)', '(S)', '(D)'
        if loc[0] == 0:
            W = '( )'
        if loc[1] == 0:
            A = '( )'
        if loc[0] == n-1 :
            S = '( )'
        if loc[1] == n-1:
            D = '( )'

        move = input(f'\t \t \t    {W}\n Enter WASD (or QUIT): {A}  {S}  {D}\n')
        
        if (move == 'A' or move == 'a') and A == '(A)':
            return 'A'
        elif (move == 'W' or move == 'w') and W == '(W)':
            return 'W'
        elif (move == 'S' or move == 's') and S == '(S)':
            return 'S'    
        elif (move == 'D' or move == 'd') and D == '(D)':
            return 'D'
        elif move == 'quit' or move == 'QUIT':
            print('Byeeee :)')
            sys.exit()
        else:
            print('Invalid move')


#Part 2

def makeMove(grouped, move):
    n = len(grouped[0])
    loc = findEmptyTile(grouped)

    if move == 'A' and loc[1] != 0:
        (grouped[loc[0]][loc[1]], grouped[loc[0]][loc[1]-1]) = (grouped[loc[0]][loc[1]-1], grouped[loc[0]][loc[1]])

    elif move == 'W' and loc[0] != 0:
        (grouped[loc[0]][loc[1]], grouped[loc[0]-1][loc[1]])  = (grouped[loc[0]-1][loc[1]], grouped[loc[0]][loc[1]])

    elif move == 'S' and loc[0] != n-1:
        (grouped[loc[0]][loc[1]], grouped[loc[0]+ 1][loc[1]]) = (grouped[loc[0]+ 1][loc[1]], grouped[loc[0]][loc[1]]) 

    elif move == 'D' and loc[1] != n-1:
        (grouped[loc[0]][loc[1]], grouped[loc[0]][loc[1]+1]) = (grouped[loc[0]][loc[1]+1], grouped[loc[0]][loc[1]])
    
#Main program

input('''Welcome to the Sliding Puzzle Game!
Here are the rules:
- Arrange tiles in order by sliding them into the empty space.
- Move tiles adjacent to the empty space (left, right, up, down).
- Win by ordering all tiles with the empty space at the bottom-right.
- Have fun!\n''')

e = int(input('Enter the number that will be the side length of the square board: '))
x = getNewPuzzle(e)
move_count = 0
while True:
    n = len(x)
    correct_order = [f'{i} ' for i in range(1, n**2)] + ['  ']  # Correct sequence
    current_order = [x[i][j] for i in range(n) for j in range(n)]
    move_count += 1
    if correct_order == current_order:
        displayBoard(x)
        print(f'Congratulations! You solved the puzzle using {move_count -1} moves')
        break  
    if move_count == 32 and e == 3:
        print('Out of moves! Better luck next time!')
        sys.exit()
    elif move_count == 81 and e == 4:
        print('Out of moves! Better luck next time!')
        sys.exit()
    move = nextMove(x)
    makeMove(x, move)

