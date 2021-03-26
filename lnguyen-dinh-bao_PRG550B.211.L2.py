def drawPascalsTriangle(n):

    for i in range(1, n+1): 
        C = 1

        for j in range(1, i+1): 
            if(j ==i):
                print(C, sep='', end='')
            else:
                print(C," ", sep='', end='') 
            C = C * (i - j) // j 
            
        print() 
    

def alphaFrequency(userString):
    print(userString)
    alphabet = string.ascii_lowercase
    userString=userString.lower()
    userString=sorted(userString)
    myDict = {}
    for i in userString: 
        if i in myDict: 
            myDict[i] += 1
        else: 
            myDict[i] = 1
    for i in myDict:
        if i in alphabet:
            print(i,"=",str(myDict[i]),"*"*myDict[i])

def encryptStr(userString, n):
    alphabet = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase
    encrypted = ""
    if(n>25):
        n=n%26
    for letter in userString:
        if letter in alphabet:
            if (int(ord(letter)+n))<123:
                encrypted+= chr((ord(letter)+n))
            else:
                encrypted+=chr(int(ord(letter)-(26-n)))
        elif letter in alphabetUpper:
            if (int(ord(letter)+n))<91:
                encrypted+= chr((ord(letter)+n))
            else:
                encrypted+=chr(int(ord(letter)-(26-n)))
        else:
            encrypted+=letter
    print(encrypted)


    
