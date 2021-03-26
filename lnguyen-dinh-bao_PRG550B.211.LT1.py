def loadDataIntoDictionary(fn) :
    distanceDict ={}
    data = []
    count =0
    f = open(fn, "r")
    with open(fn) as openfileobject:
        for line in openfileobject:
            data = f.readline().split(':')
            data[2]=data[2].replace('\n','')
            distanceDict[data[0]] = [data[1],data[2]]
            count+=1
        print(count,"city records loaded...")
    return distanceDict
        
def computeDistance(table, cityFrom, cityTo) :
    city1 = 0
    city2 = 0
    name1 =""
    name2 =""
    distance =0 
    for x in table:
        a = table[x]
        if x.lower()==cityFrom.lower():
            city1 = a[1]
            name1 =x
        if x.lower()==cityTo.lower():
            city2 = a[1]
            name2=x
    
    if(float(city1)>float(city2)):
        distance = float(city1) -float(city2)
    else:
        distance = float(city2)-float(city1)
    if city1==0 or city2==0:
        print("ERROR... one or more city names NOT found!")
    else:
        print("distance from ",name1,", ",table[name1][0]," to ",name2,", ",table[name2][0]," is: ",float("{:.3f}".format(distance))," km",sep='')


    



