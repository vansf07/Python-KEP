keys = []

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

for key in board:
    keys.append(key)

# printing the board after updating every move
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def tictactoe():
    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(board)
        print("Player " + turn + "'s turn, Enter your position: ")

        move = input()        

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("This position is filled filled.\nEnter your position again: ")
            continue
        # after 5 moves, check if either player has won by checking rows, columns, diagonals
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': 
                printBoard(board)
                print("\nGame Over!!")                
                print(turn + " won!!")
                break 

        # if board is full with no winner
        if count == 9:
            print("\nIt's a Draw :(\n")                

        # Changing player for next move
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do you want to play again? (y/n)")
    if restart == "y" or restart == "Y":  
        for key in keys:
            board[key] = " "

        tictactoe()

if __name__ == "__main__":
    print("Positions on board are from 1 - 9")
    print("***********************************")
    tictactoe()