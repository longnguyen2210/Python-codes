import math
import random
import string
import collections
import datetime
import re
import time
import copy
def generateGameBoard(nRows, nCols) : 
    board = [["." for a in range(nCols)] for a in range(nRows)]
    return board

def loadWord(boardData, nRows, nCols, coord, word, dir) :

    
    if re.search("^[A-Z]$",coord[0]):
        r = ord(coord[0]) - 56
    else :
        r = int(coord[0])-1
    if re.search("^[A-Z]$",coord[1]):
        c = ord(coord[1]) - 56
    else :
        c = int(coord[1])-1
    
    if(dir =='H'):
        for letter in range(0,len(word)):
            boardData[r][c+letter] = word[letter]
    elif dir =='V':
        for letter in range(len(word)):
            boardData[r+letter][c] = word[letter]
    return boardData


def checkCoord(nRows, nCols, coord) :
    row = coord[0]
    col = coord[1]
    if re.search("^[A-Z]$",coord[0]):
        row = ord(coord[0]) - 56
    else :
        row = int(coord[0])-1
    if re.search("^[A-Z]$",coord[1]):
        col = ord(coord[1]) - 56
    else :
        col = int(coord[1])-1
    if re.search("^[A-Z1-9]{2}$",coord):

        if(int(row)<nRows):
            if int(col) <= nCols:
                return True
        else:
            return False

def updateGameBoard(boardData, boardMask, nRows, nCols, coord, score, lastMove) :
    count=1
    row = coord[0]
    col = coord[1]
    if re.search("^[A-Z]$",coord[0]):
        row = ord(coord[0]) - 56
    else :
        row = int(coord[0])-1
    if re.search("^[A-Z]$",coord[1]):
        col = ord(coord[1]) - 56
    else :
        col = int(coord[1])-1
    baseRow = row
    baseCol = col
    if(checkCoord(nRows,nCols,coord)):
        if boardData[row][col] != '.' and boardData[row][col] != '~' :
            boardMask[row][col] = boardData[row][col]
            row+=1
            while (boardData[row][col] != '.' and boardData[row][col] != '~') and ((row<=nRows and row >=0)and(col<=nCols and col >=0)):
                if boardMask[row][col] != boardData[row][col]:
                    score+=5
                boardMask[row][col] = boardData[row][col]
                row+=1
                
            row=baseRow-1
            while(boardData[row][col] != '.' and boardData[row][col] != '~')and ((row<=nRows and row >=0)and(col<=nCols and col >=0)):
                if boardMask[row][col] != boardData[row][col]:
                    score+=5
                boardMask[row][col] = boardData[row][col]
                row-=1
                
            row=baseRow
            col+=1
            while(boardData[row][col] != '.' and boardData[row][col] != '~')and ((row<=nRows and row >=0)and(col<=nCols and col >=0)):
                if boardMask[row][col] != boardData[row][col]:
                    score+=5
                boardMask[row][col] = boardData[row][col]
                col+=1
                
            col=baseCol-1
            while(boardData[row][col] != '.' and boardData[row][col] != '~')and ((row<=nRows and row >=0)and(col<=nCols and col >=0)):
                if boardMask[row][col] != boardData[row][col]:
                    score+=5
                boardMask[row][col] = boardData[row][col]
                col-=1
                
            score+=5
            print("  Python Crossword Puzzle...\n  123456789ABCDEFGHIJKLMNOPQ")
            for ro in boardMask:
                if(count>9):
                    count =chr(count+55)
                    print(count,"|", end="", sep="")
                    count=ord(count) -55
                    count+=1
                else:
                    print(count,"|", end="", sep="")
                    count+=1
                for co in ro:
                    print(co ,end="" ,sep="")
                print("|" , sep="")
            print("Current Score:","{:04d}".format(score),end="")
            print("  Last Move: FOUND '",boardData[baseRow][baseCol], "'at [",coord[0],",",coord[1],"]",sep="")
            
        else:
            boardMask[baseRow][baseCol] ='~'
            print("  Python Crossword Puzzle...\n  123456789ABCDEFGHIJKLMNOPQ")
            for ro in boardMask:
                if(count>9):
                    count =chr(count+55)
                    print(count,"|", end="", sep="")
                    count=ord(count) -55
                    count+=1
                else:
                    print(count,"|", end="", sep="")
                    count+=1
                for co in ro:
                    print(co ,end="" ,sep="")
                print("|" , sep="")
            print("Current Score:","{:04d}".format(score),end="")
            print("  Last Move: NO letter FOUND at [",coord[0],",",coord[1],"]")
                 
    else:
        print("  Python Crossword Puzzle...\n  123456789ABCDEFGHIJKLMNOPQ")
        for ro in boardMask:
            if(count>9):
                count =chr(count+55)
                print(count,"|", end="", sep="")
                count=ord(count) -55
                count+=1
            else:
                print(count,"|", end="", sep="")
                count+=1                
            for co in ro:
                print(co ,end="" ,sep="")
            print("|" , sep="")
        print("Current Score:","{:04d}".format(score),end="")
        print("  Last Move:  [",coord[0],",",coord[1],"] is an INVALID COORDINATE")
           
    return boardData, boardMask, score, lastMove
        
def main( ) :
    score = 0
    coords = [ "25", "2A", "XL", "9Q", "1D", "6J", "93", "B4", "AF" ]
    lastMove = ""
    board = generateGameBoard(20, 26)
    mask = generateGameBoard(20, 26)

    board = loadWord(board, 20, 26, "29", "HELLO", "H") # loading words onto game board
    board = loadWord(board, 20, 26, "1D", "NO", "V")
    board = loadWord(board, 20, 26, "2A", "EXAMINE", "V")
    board = loadWord(board, 20, 26, "5J", "AREA", "V")
    board = loadWord(board, 20, 26, "6H", "NORTH", "H")
    board = loadWord(board, 20, 26, "93", "PYTHON", "H")
    board = loadWord(board, 20, 26, "AD", "PUZZLE", "H")
    board = loadWord(board, 20, 26, "B4", "7-SEAS", "H")
    board = loadWord(board, 20, 26, "AF", "ZOO", "V")

    for coord in coords :
        (board, mask, score, lastMove) = updateGameBoard(board, mask, 20, 26, coord, score, lastMove)
        print( )

if __name__ == "__main__" :
    main( )

