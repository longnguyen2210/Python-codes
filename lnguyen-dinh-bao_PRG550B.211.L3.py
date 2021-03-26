def loadDictionary(book, sequence, key = 'X') :
    
    book[key] = sequence
    return book
def dotProduct(myDictParam) :
    resultList =[1]* len(next(iter(myDictParam.values())))  
    for i in myDictParam:
         resultList = [a * b for a, b in zip(resultList, myDictParam[i])]
    result = reduce(lambda c,d: c+d ,resultList)
    return result
def integerToRoman(n) :
   romans = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M" }
   romanString = ""
   th = 0
   if n < 1 or n > 3999 :
      romanString = "Invalid"
   else : # computations
        th = int(n / 1000)  # thousands
        for i in range(th) :
            romanString += romans[1000]
            n -= 1000
        if((n%1000)>=900):
            romanString += romans[100]+romans[1000]
            n -= 900
         
            
            
        
        hth = int(n/500)
        for j in range(hth):
            romanString += romans[500]
            n -= 500
        if(((n%1000)>=400)and((n%1000)<500)):
            romanString += romans[100]+romans[500]
            n -= 400
        
            
            
        
        hr = int(n/100)
        for j in range(hr):
            romanString += romans[100]
            n -= 100
        
        if(((n%100)>=90)and((n%100)<100)):
            romanString += romans[10]+romans[100]
            n -= 90
        
        hhr = int(n/50)
        for j in range(hhr):
            romanString += romans[50]
            n -= 50
        if(((n%100)>=40)and((n%100)<50)):
            romanString += romans[10]+romans[50]
            n -= 40
        
            
           
        
        ten = int(n/10)
        for j in range(ten):
                romanString += romans[10]
                n -= 10
        if(((n%100)>=9)and((n%100)<10)):
            romanString += romans[1]+romans[10]
            n -= 9
       
            
            
        
        fi = int(n/5)
        for j in range(fi):
            romanString += romans[5]
            n -= 5
        if(((n%10)>=4)and((n%10)<5)):
            romanString += romans[1]+romans[5]
            n -= 4
        
            
            
        
        one = int(n/1)
        for j in range(one):
            romanString += romans[1]
            n -= 1
        
        
        


   return romanString    
    
    
