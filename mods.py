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



def binaryToInt(_binNum):
    tmpsum = 0
    for i in range(len(_binNum)):
        if int(_binNum[len(_binNum)-i-1]) == 1:
            tmpsum += 2**i
    return tmpsum

def binaryAdd(x, y): #takes lists ([0,0,1,0],[1,0,1])
    rx = revArray(x)
    ry = revArray(y)
    if len(x) != len(ry):
        if min(len(x),len(y)) == len(x):
            s = rx
        else:
            s = ry
    while len(rx) != len(ry):
        s.append(0)

    carry = 0
    sum = []
    for i in range(len(rx)):
        if rx[i] and ry[i] and carry:
            sum.append(1)
            carry =1
        elif (rx[i] and ry[i] and not carry) or (rx[i] and carry and not ry[i]) or (ry[i] and carry and not rx[i]):
            sum.append(0)
            carry = 1
        elif (rx[i] and not carry and not ry[i]) or (carry and not rx[i] and not ry[i]) or (ry[i] and not carry and not rx[i]):
            sum.append(1)
            carry = 0
        else: #all 0s
            sum.append(0)
            carry=0
    if carry:
        sum.append(1)
    return(revArray(sum))

l = []
o = []
l.append(int(1))
l.append(int(1))
l.append(int(1))
print(l)
print(binaryToInt(l))
print("+")
    
o.append(int(1))
o.append(int(1))
o.append(int(1))
o.append(int(1))
print(o)
print(binaryToInt(o))


h = binaryAdd(l,o)
print(h)
print("=")
print(binaryToInt(h))


def mult(x, y):
    rval = int(0)
    for i in range(y):
        tmpsum = binaryAdd(numToBinary(x), numToBinary(rval))
        print(tmpsum)
        rval += binaryToInt(tmpsum)
        print(binaryToInt(int(rval)))
    return int(rval)

def binMult(x, y):
    rsum = 0
    
    print(binaryToInt(y))
    for i in range(binaryToInt(y)):
        print("rsum:")
        print(rsum)
        tmp = binaryAdd(numToBinary(rsum), x)
        rsum = binaryToInt(tmp)
        
    return rsum

x = []
y = []
x.append(int(1))
x.append(int(1)) #x=3

y.append(int(1)) #y = 5
y.append(int(0))
y.append(int(1))
print(binMult(x,y))
