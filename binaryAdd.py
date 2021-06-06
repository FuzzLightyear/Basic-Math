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
   
        #tempsum = []\n",
        #for i in range(length):\n",
m = []
n = []
m.append(int(1))
m.append(int(0))
m.append(int(1))
    
n.append(int(1))
n.append(int(0))
n.append(int(1))

z = binaryAdd(m,n)

print(z)