import random #to be used later for random move generation
import os#for ocassionally clearing the screen

def cls():#a function to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

#-----------------------------------------------------------------

def boardPrint(): #displays the board
    global board
    fiveSpaces=' '*5
    print('\n') #two blank lines for clarity's sake
    print(fiveSpaces,end='')
    for i in [7,8,9,4,5,6,1,2,3]:#to match keyboard numpad

        if i % 3 !=0:#to avoid '|' at the end of a row  
            print(board[i],'|',end=' ')

        else: #to insert new line at end of row
            print (board[i],end='\n')
            print(fiveSpaces,end='')
            
            if i !=3:
                print('---------')#no '--------' after last row
                print(fiveSpaces,end='')

        continue
    
    print('\n') #two blank lines for clarity's sake
    return
#----------------------------------------------------------------------------


#note that variable move is used thrice, each time locally, never globally            
        
def boardManager(move):        #makes changes to the board according to given move
    global board,currentPlayer

    board[move]=currentPlayer
    return
#----------------------------------------------------------------------------

    
#Inputs the human player's move and returns it 
def human():
    global humanPlayer

    move='whatever' #initializing move before while loop

    while move not in board :
        move=input(str(humanPlayer)+' moves:')
        continue
    move=int(move)#move is not made int at input time to account for mismatched string inputs

    return move

#----------------------------------------------------------------------------

    
def ai(): #decides the computer's moves
    global board, aiPlayer, humanPlayer
    aiMove='whatever' #initializing aiMove
    
    ''' for ease in going through all the different possibilities of moves, we
    shall define a list of integars. These integars are indexes of the list board
    and are arranged in groups of three. First two members of each group are the
    indexes to be compared and the third is the index which is to be assigned the
    value of aiPlayer if the first two are equal. This list will allow us to make
    all comparisons in a single for loop
    '''
    possibilityList=[1,2,3,     2,3,1,      1,3,2,#first row
                     4,5,6,     5,6,4,      4,6,5,#second row
                     7,8,9,     8,9,7,      7,9,8,#third row
                     1,4,7,     4,7,1,      1,7,4,#first column
                     2,5,8,     5,8,2,      2,8,5,#second column
                     3,6,9,     6,9,3,      3,9,6,#third column
                     1,5,9,     5,9,1,      1,9,5,#main diagonal
                     3,5,7,     5,7,3,      7,3,5]#secondary diagonal
    #first computer checks for a chance to secure a win
    
    for i in range(0,len(possibilityList),3):
        if (board[possibilityList[i]]==board[possibilityList[i+1]]==aiPlayer) and board[possibilityList[i+2]]!='X' and board[possibilityList[i+2]]!='O':
            aiMove= possibilityList[i+2]
            break
        continue

    #then computer attempts to prevent a loss
    
    if aiMove == 'whatever':#so this code not executed if move already decided
        for i in range(0,len(possibilityList),3):
            if board[possibilityList[i]]==board[possibilityList[i+1]]==humanPlayer and board[possibilityList[i+2]]!='X' and board[possibilityList[i+2]]!='O':
                aiMove= possibilityList[i+2]
                break
            continue

    #if there is no chance of winning or loosing, the computer shall
    #attempt to move at the centre, because thats how i play in real life

    if aiMove == 'whatever':#so this code not executed if move already decided
        if board[5] =='5':
            aiMove= 5

    #if centre already taken, then a random move is returned
            
    if aiMove == 'whatever':#so this code not executed if move already decided
        while True:
            randomMove=random.randint(1,9)
            if str(randomMove) in board:# ensures only a valid random move is returned
                aiMove= randomMove
                break
            continue
    print(aiPlayer,'moves:'+str(aiMove))
    return aiMove
    

#----------------------------------------------------------------------------
def judge():#returns the state of the match
    global board,moveCount

    

    #checking for a win in the rows
    for a in range(1,10,3):                 #a takes values 1,4,7 corresponding to 1st number of each row
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

#----------------------------------------------------------------------------





#main program starts here
while True: #program repeats until closed via os
    board=[str(i) for i in range(10)]#board[0] to be ignored for simplicity & readibilty. board[1:9] to represent
                                #the 9 squares of a tic tac toe board



    #deciding player deignation as x or o:

    playerInput='something' #initializing

    while playerInput.lower() !='x' and playerInput.lower() != 'o': 

        playerInput=input('Would you like to take X or O (X goes first):')
        continue

    if playerInput.lower()=='x':
        humanPlayer='X'
        aiPlayer='O'

    else:
        humanPlayer='O'
        aiPlayer='X'#end of desigantion process
        
    moveCount=0
    #starting the game loop:

    while judge()=='continue':
        
        boardPrint()

        if moveCount %2==0:     
            currentPlayer='X'   #as X goes first so gets even numbered moves
        else :
            currentPlayer='O'
            

        if currentPlayer==humanPlayer:
            boardManager(human())
            
        else:
            cls()
            boardManager(ai())
        moveCount += 1
        continue
    
    cls()
    boardPrint()
    
    if judge()=='win':
            print(currentPlayer,'wins.')
    else:
        print ('Match Drawn')

    restart=input('Press enter to restart or type exit to exit:')
    if restart=='exit':
        break;
    cls()
    continue

#-------------------------------------------------------------------------------
    
        


    
    


    

        









