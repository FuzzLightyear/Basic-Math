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
    print("Adding Binary Numbers: ", x , " (", binaryToInt(x), ")    and    ", y, " (", binaryToInt(y), ")")
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

o.append(int(1))
o.append(int(1))
o.append(int(1))
o.append(int(1))

print("Proceeding with binary number addition of X and Y to get sum Z")
print("X, as seen directly below in binary and numerical form")
print(l)
print(binaryToInt(l))
print("+")

print("Y, as seen directly below in binary and numerical form")

print(o)
print(binaryToInt(o))


h = binaryAdd(l,o)
print(h)
print("=")
print("Z, as seen directly below in binary and numerical form")
print(binaryToInt(h))


def binMult(x, y):
    rsum = 0
    print(binaryToInt(y))
    for i in range(binaryToInt(y)):
        tmp = binaryAdd(numToBinary(rsum), x)
        rsum = binaryToInt(tmp) 
    return tmp #return rsum to return int

def mult(x, y):
    #Proceeding with multiplication.
    #Converted x and y to binary forms. 
    #Transitioning to binary multiplication operation.
    binProduct = binMult(numToBinary(x), numToBinary(y))
    return(binaryToInt(binProduct))

def add(x, y):
    #Proceeding with addition.
    #Converted x and y to binary forms. 
    #Transitioning to binary addition operation.
    binSum = binaryAdd(numToBinary(x), numToBinary(y))
    return(binaryToInt(binSum))

# x = []
# y = []
# x.append(int(1))
# x.append(int(1)) #x=3

# y.append(int(1)) #y = 7
# y.append(int(1))
# y.append(int(1))
# print(binMult(x,y))

print(mult(5, 7))
print(add(3,10))
