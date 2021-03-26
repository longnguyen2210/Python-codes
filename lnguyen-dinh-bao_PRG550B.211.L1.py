def drawTriangle(rows):
    pyramidValues = string.digits
    for level in range(0,rows):
        leftSide = list(pyramidValues[0:level])
        sides = ["".join(leftSide) , "".join(leftSide[::-1])]
        if (level==0):
            print(" "*(int(rows)-1-int(level)), 0)
        else:
            print(" "*(int(rows)-1-int(level)), str((level)).join(sides))
        
        
def threeLetterCombinations(letter):
    
    for firstLetter in range(97,(ord(letter)+1)):
        for secondLetter in range(97,(ord(letter)+1)):
            for thirdLetter in range(97,(ord(letter)+1)):
                combination = chr(int(firstLetter)) +" "+ chr(int(secondLetter)) +" "+ chr(int(thirdLetter))
                print(combination)
                
                    
                
def allNarcissisticNumbers(limit):
    sum = 0
    for num in range(10,limit+1):
        numStr = str(num)
        numLen = len(numStr)
        sum = 0
        for index in range(0,(int(numLen))):
            sum = sum + int(numStr[index])**int(numLen)
        if(sum == num):
            print(num)



        
