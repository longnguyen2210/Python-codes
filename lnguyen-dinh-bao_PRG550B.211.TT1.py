def checkRegex(inputC):
    a=0
    b=0
    c=0
    if(inputC[0].isalpha() and len(inputC)>7):
        for char in inputC:
            if(char.isupper()):
                a=a+1
            if(char.islower()):
                b=b+1
            if char in "* - @ # $ . | / \ !":
                c=c+1
        if(a>0 and b>0 and c>0)  :
            return True     
        else:
            return False
        
                    
           

    else:
        return False
def fancyList():
    print([x*5 for x in string.ascii_uppercase if x in"AEIOU"])

def printEvens(a,b):
    myList=[]
    
    for a in range(a,b):
        for char in str(a):
            if int(char)%2==1:
                break
        else:
            myList.append(a)
    return print(myList)
def generatePokerHand(deck,coords):
    row=0
    column=0
    newString=""
    for card in coords:
        row=int(card[0])
        if card[1]=='A':
            column=10
        elif card[1]=='B':
            column=11
        elif card[1]=='C':
            column=12
        else:
            column=int(card[1])
        if(card==coords[-1]):
            newString+=deck[row][column]
        else:
            newString+=deck[row][column]+'-'

    return print(newString)

def natureSequence(fn,sn,n):

    def recur_fibo(fn,sn,a):
        
        if a == 0:
            return fn
        elif a == 1 :
            return sn
    
        else:
            return recur_fibo(fn,sn,a-1) + recur_fibo(fn,sn,a-2)
    for a in range(n):
        if(a==n):
            print(recur_fibo(fn,sn,a),end="")
        else:
            print(recur_fibo(fn,sn,a),"",end="")
    print("")
    return print(recur_fibo(fn,sn,a) / recur_fibo(fn,sn,a-1))
    




    