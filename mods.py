#Author FuzzLightyer aka Fuzzifier aka Medusa
#File to store some of the functions defined elsewhere

def getPhi(): #input(None), calculates phi. Returns phi
    n = 20
    print(n)
    phi = 1.00
    current = 1.00
    last = 1.00
    tmp = 1.00
    for i in range(n):
        print("current:",current,";  last:",last,";")
        tmp = current
        current = current + last
        last = tmp
        phi = (phi+(current/last))/2
    return phi


def revArray(x): #input(list), makes new list with elements in reverse order, returns reversed array
    #set reverse arrays
    revx = list()
    bc = len(x)-1
    for rx in range(len(x)):
        revx.append(x[bc])
        bc = bc - 1
    return revx



def numToBinary(x):
    tmpx = x
    counter = 0
    binNum = []
    while 2**counter <= x: #If less than 8 for example, must only need 3 digits
        counter += 1
    for i in range(counter):
        if tmpx - 2**(counter-i-1) >= 0: #if can subtract by next highest power of 2, do it and append 1 to binNum. 
            tmpx -= 2**(counter-i-1) #Set tmpx as remainder of the subtraction
            binNum.append(int(1)) #mark in binNum that this operation was done successfully
        else:
            binNum.append(int(0))
    return binNum
print(numToBinary(15))


def binaryToInt(_binNum):
    tmpsum = 0
    for i in range(len(_binNum)):
        if int(_binNum[len(_binNum)-i-1]) == 1:
            tmpsum += 2**i
    return tmpsum

def binaryAdd(x, y): #takes lists ([0,0,1,0],[1,0,1])
    length = 0
    tmp = []
    if len(x) >= len(y):
        g = x
        s = y
    else:
        g = y
        s = x
    length = len(g)
    for i in range(len(g)-len(s)):
        s.insert(0, 0)
    
    carry = 0
    for j in range(length):
        if carry == 0:
            if x[len(x)-j-1] == 0:
                if y[len(y)-j-1] == 0:
                    carry = 0
                    tmp.insert(j, 0)
                else: #y[len(y)-j] == 1
                    carry = 0
                    tmp.insert(j, 1)
            else: #x 1
                if y[len(y)-j-1] == 0:
                    carry = 0
                    tmp.insert(j, 1)
                else: #y 1 x 1 c 0
                    carry = 1
                    tmp.insert(j, 0)
        else: #c 1
            if x[len(x)-j-1] == 0:
                if y[len(y)-j-1] == 0: #c1 x0 y0
                    carry = 0
                    tmp.insert(j, 1)
                else: # c1 x0 y1
                    carry = 1
                    tmp.insert(j, 0)
            else:
                if y[len(y)-j-1] == 0: #c1 x1 y0
                    carry = 1
                    tmp.insert(j, 0)
                else: #c1 x1 y1
                    carry = 1
                    tmp.insert(j, 1)

    if carry == 1:
        tmp.insert(0, 1)

    print(x)
    print(" + ")
    print(y)
    print("=")
    return tmp


def mult(x, y):
    rval = int(0)
    for i in range(y):
        tmpsum = binaryAdd(numToBinary(x), numToBinary(rval))
        rval += binaryToInt(tmpsum)
        print(binaryToInt(int(rval)))
    return int(rval)

print(binaryToInt([1,1,0]))
