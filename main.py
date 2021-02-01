import sys
from termcolor import colored

def drawBoard(field):
    for row in range(13):
        if row%2==0:
            practicalRow = int(row/2)
            for column in range(13):
                if column%2==0:
                    practicalColumn = int(column/2)
                    if column!=12:
                        print(field[practicalColumn][practicalRow],end='')
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print('|',end='')
        else:
            print('-------------')

currentField = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
player = 1
while(True):
    horizontalCounter=0
    verticalCounter=0
    Diagonal1Counter=0
    Diagonal2Counter=0
    Diagonal3Counter=0
    Diagonal4Counter=0
    print('Player '+str(player)+' turn:')
    moveColumn = int(input('Select the column:\n'))
    for moveRow in range(6,-1,-1):
        if currentField[moveColumn][moveRow] == ' ':
            #If player 1's turn
            if player==1:
                currentField[moveColumn][moveRow]=colored('O','red')
                #check for 4 vertical across
                for row in range(6,-1,-1):
                    if currentField[moveColumn][row]==colored('O','red'):
                        verticalCounter+=1
                        if verticalCounter==4:
                            break
                    else:
                        verticalCounter = 0
                #check for 4 horizontal across
                for col in range(6,-1,-1):
                    if currentField[col][moveRow]==colored('O','red'):
                        horizontalCounter+=1
                        if horizontalCounter==4:
                            break
                    else:
                        horizontalCounter=0
                #check for 4 diagonal across
                diagonalRange=0
                if moveColumn>moveRow:
                    diagonalRange=moveColumn-moveRow
                    row=0
                    #check for 4 diagonal across (left to right)
                    for col in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','red'):
                            Diagonal1Counter+=1
                            if Diagonal1Counter==4:
                                break
                        else:
                            Diagonal1Counter=0
                        row+=1
                    
                    col=6
                    #check for 4 diagonal across (right to left)
                    for row in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','red'):
                            Diagonal2Counter+=1
                            if Diagonal2Counter==4:
                                break
                        else:
                            Diagonal2Counter=0
                        col-=1
                   
                else:
                    diagonalRange=moveRow-moveColumn
                    col=0
                    #check for 4 diagonal across (left to right)
                    for row in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','red'):
                            Diagonal3Counter+=1
                            if Diagonal3Counter==4:
                                break
                        else:
                            Diagonal3Counter=0
                        col+=1

                    row=6
                    #check for 4 diagonal across (right to left)
                    for col in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','red'):
                            Diagonal4Counter+=1
                            if Diagonal4Counter==4:
                                break
                        else:
                            Diagonal4Counter=0
                        row-=1
            else:
                #If player 2's turn
                currentField[moveColumn][moveRow]=colored('O','green')
                #check for 4 vertical across
                for row in range(6,-1,-1):
                    if currentField[moveColumn][row]==colored('O','green'):
                        verticalCounter+=1
                        if verticalCounter==4:
                            break
                    else:
                        verticalCounter = 0
                #check for 4 horizontal across
                for col in range(6,-1,-1):
                    if currentField[col][moveRow]==colored('O','green'):
                        horizontalCounter+=1
                        if horizontalCounter==4:
                            break
                    else:
                        horizontalCounter=0
                #check for 4 diagonal across
                diagonalRange=0
                if moveColumn>moveRow:
                    diagonalRange=moveColumn-moveRow
                    row=0
                    #check for 4 diagonal across (left to right)
                    for col in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','green'):
                            Diagonal1Counter+=1
                            if Diagonal1Counter==4:
                                break
                        else:
                            Diagonal1Counter=0
                        row+=1
                    
                    col=6

                    #check for 4 diagonal across (right to left)
                    for row in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','green'):
                            Diagonal2Counter+=1
                            if Diagonal2Counter==4:
                                break
                        else:
                            Diagonal2Counter=0
                        col-=1
                   
                else:
                    diagonalRange=moveRow-moveColumn
                    col=0
                    #check for 4 diagonal across (left to right)
                    for row in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','green'):
                            Diagonal3Counter+=1
                            if Diagonal3Counter==4:
                                break
                        else:
                            Diagonal3Counter=0
                        col+=1

                    row=6
                    #check for 4 diagonal across (right to left)
                    for col in range(diagonalRange,7):
                        if currentField[col][row]==colored('O','green'):
                            Diagonal4Counter+=1
                            if Diagonal4Counter==4:
                                break
                        else:
                            Diagonal45Counter=0
                        row-=1
            break
    if verticalCounter==4 or horizontalCounter ==4 or Diagonal1Counter==4 or Diagonal2Counter==4 or Diagonal3Counter==4 or Diagonal4Counter==4:
        drawBoard(currentField)
        print('Player '+str(player)+' wins!')
        break
    if player==1:
        player=2
    else:
        player=1
    drawBoard(currentField)