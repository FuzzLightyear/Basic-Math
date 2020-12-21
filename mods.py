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




def binAdd(x, y): #input 2 lists of 0s and 1s (int in binary form), add them in binary, return sum in binary form
    cpx = x.copy()
    cpy = y.copy()
    #reverse so index 0 has value of max index
    cpx = revArray(cpx)
    cpy = revArray(cpy)

    #cpx/y will have same length as 1=01 in binary
    #Make array lengths equal
    if len(x) > len(y):
        big = 3
    elif len(y) > len(x):
        big = 4
    else:
        big = 0
    while big != 0:
        if big == 3:
            cpy.append(0)
        else:
            cpx.append(0)
        if len(cpx) == len(cpy):
            big = 0
   
    cpx.append(0)
    cpy.append(0)
    
    print("cpx",revArray(cpx))
    print("cpy",revArray(cpy))
    #Add by lowest digit
    z = list()
    carry = False
    for i in range(len(cpx)):
        #if 1 and 1
        if cpx[i] and cpy[i]:
            #if 1 and 1 and carry=True
            if cpx[i] and carry:
                z.append(1)
            #if 1 and 1 and carry=False
            else:
                carry = True
                z.append(0)
        #if 1 and 0
        elif cpx[i] or cpy[i]:
            if carry:
                z.append(0)
            else:
                z.append(1)
        #if 0 and 0
        else:
            if carry:
                z.append(1)
                carry = False
            else:
                z.append(0)
        print(z)
        z = revArray(z)
    return z

def numToBin(x): #input int, returns list of 0s and 1s equal to binary version, return binary version of the int
    listSize = 0
    #if 15, 1<15,2<15,4<15,8<15,16>15
    #        0    1    2    3      4
    for listSize in range(10):
        if 2**listSize > x:
            break
            
    backCount = listSize -1 
    staticNum = x
    binNum = list()
    for i in range(listSize):
        if staticNum >= 2**backCount:
            print(staticNum, ">= ",2**backCount, "remainder", staticNum- 2**backCount)
            staticNum = staticNum - (2**backCount)
            binNum.append(1)
            
        else:
            binNum.append(0)
        backCount = backCount-1
    return binNum

def binToInt(x): #input binary number (list of 0s and 1s), return int value
    count = 0
    z = revArray(x)
    for i in range(len(z)):
        tmp = z[i] * 2**i
        count = count + tmp
    return count
def add(x, y): #input 2 ints, translates them to binary, sends them to binary add, translates their binary sum into int version and returns int
    #ints x and y into binary (list of 0/1s)
    x = numToBin(x)
    y = numToBin(y)
    #add
    z = binAdd(x, y)
    print(x)
    print(y)
    print(z)
    

    v = binToInt(z)
    return v

def Multiply(x, count):
    rval = 0
    for i in range(count):
        rval = add(x, rval)
        print(rval)
    return rval