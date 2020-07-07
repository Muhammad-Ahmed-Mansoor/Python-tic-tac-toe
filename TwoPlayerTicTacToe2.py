import os;

def boardPrint(): #displays the board
    global board

    print('\n') #two blank lines for clarity's sake

    for i in [7,8,9,4,5,6,1,2,3]:#to match keyboard numpad

        if i % 3 !=0:#to avoid '|' at the end of a row  
            print(board[i],'|',end=' ')

        else: #to insert new line at end of row
            print (board[i])
            
            if i !=3:
                print('---------')#no '--------' after last row

        continue
    
    print('\n') #two blank lines for clarity's sake
    return




#note that variable move is use twice, each time locally, never globally            
        
def boardManager(move):        #makes changes to the board according to given move
    global board,currentPlayer

    board[move]=currentPlayer
    return


    

def moveInput():
    global currentPlayer

    move='whatever' #initializing move before while loop

    while move not in board :
        move=input(currentPlayer+' moves:')
        continue
    move=int(move)#move is not made int at input time to account for mismatched string inputs

    return move



def judge():#returns the state of the match
    global board,moveCount

    

    #checking for a win in the rows
    for a in range(1,10,3):                 #a takes values 1,4,7
        if board[a]==board[a+1]==board[a+2]:#checks an entire row for equality
            return 'win'
        continue
    

    #checking for a win in the columns
    for b in range(1,4):
        if board[b]==board[b+3]==board[b+6]:#checks an entire column for equality
            return 'win'
        continue

    #checking for a win in diagonals
    if board[1]==board[5]==board[9] or board[3]==board[5]==board[7]:
        return 'win'

    #check for draw
    if moveCount==9:
        return 'draw'


    #if no win or draw, match continues
    return 'continue'
        




#main program starts here
while True:#so game plays until user closes
    board=[str(i) for i in range(10)]#board[0] to be ignored for simplicity & readibilty. board[1:9] to represent
                                #the 9 squares of a tic tac toe board.


    
    moveCount=0


    #starting the game loop:

    while judge()=='continue':

        if moveCount %2==0:     
            currentPlayer='X'   #as X goes first so gets even numbered moves
        else :
            currentPlayer='O'
        boardPrint()
        boardManager(moveInput())
        os.system("cls")

        moveCount+=1
        continue



    boardPrint()
    if judge()=='win':
        print(currentPlayer+' wins.')
    elif judge()=='draw':
        print ('Match Drawn')


    print()
    restart=input('Press enter to restart or type exit to exit.')
    if restart=='exit':
        break;
    os.system("cls")
    continue

    


    

        









