
test_board=['#','X','O','X','X','O','X','X','O','X']
board = ['#', '', '', '', '', '', '', '', '', '']


def display_board(board):
    print('_________________________________________')
    print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')
    print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
    print('-----------------------------------------')



##display_board(test_board)

def player_input():
    marker=''
    while marker not in ['X','O']:
        marker=input('Player 1 , choose X or O:')
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

def assign_value(player_marker,playerno):
    index_pos=0
    while index_pos not in [1,2,3,4,5,6,7,8,9]:
        index_pos=int(input('Enter '+playerno+' index postion'))
    board[index_pos]=player_marker
    return board
def isBoardFull(board):
    for item in range(1,10):
        if (board[item] == ''):
            return False
    return True

def checkForWin(board,marker):
    if(board[1]==board[2]==board[3]==marker):
        return True
    if(board[4]==board[5]==board[6]==marker):
        return True
    if(board[7]==board[8]==board[9]==marker):
        return True
    if (board[1] == board[4] == board[7] == marker):
        return True
    if (board[2] == board[5] == board[8] == marker):
        return True
    if (board[3] == board[6] == board[9] == marker):
        return True
    return False
#print(isBoardFull(board)  )
#print(isBoardFull(test_board))
#print(checkForWin(test_board,'X'))



def play_game(board):

    ready=''

    while ready not in ['YES','NO']:
        ready=input('Are you want to continue the game')


    if(ready=='YES'):
        game='ON'
       # display_board(board)
        player1,player2=player_input()
        print('Player1 marker is:'+player1)
        print('Player2 marker is:'+player2)
        while game=='ON':
            if isBoardFull(board):
                break
            board=assign_value(player1,'player1')
            display_board(board)
            if checkForWin(board,player1):
                print('Player 1 won the Match! Congrats')
                break;
            if isBoardFull(board):
                break
            board=assign_value(player2,'player2')
            display_board(board)
            if checkForWin(board,player2):
                print('Player 2 won the Match! Congrats')
                break;

        print('Game Over!')

play_game(board)




