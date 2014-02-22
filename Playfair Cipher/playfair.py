
#Hangfei Lin, and Fei Shao's Assignment3


def Keyword(S):
    a = "" 
    for i in range(0,len(S)):
        if S[i] in a:
            a = a
        else:
            a += S[i]
    return a

def Fillout(S):
    arr = []
    matrix =[[0 for x in xrange(10)] for x in xrange(10)]
    a = 0
    while a < len(S):
        arr.append(S[a])
        a += 1
    arr.append(chr(0))
    arr.append(chr(9))
    arr.append(chr(10))
    arr.append(chr(11))
    arr.append(chr(13))
    a += 5
    t = 32
    while len(S)+5 <= a < 100:
        if chr(t) in S:
            t += 1
        else:
            arr.append(chr(t))
            t += 1
            a += 1
    b = 0
    for i in range(0,10):
        for j in range(0,10):
            matrix[i][j] = arr[b]
            b += 1
    return matrix

def Textforward(S):
    i = 0
    T = []
    while i < len(S):
        if i+1 == len(S):
            T.append(S[i])
            T.append(chr(0))
            i += 1
        elif S[i] == S[(i+1)] == chr(0):
            T += S[i]
            i += 2
        elif S[i] == S[i+1]:
            T.append(S[i])
            T.append(chr(0))
            i += 1
        else:
            T.append(S[i])
            T.append(S[i+1])
            i += 2
    return T

def decode(encodedMessage,keyPhrase):
    #encodedMessage = encode("Programming in Python is fun!!","Barck H.Obm")
    decodedMessage = ""
    #print encodedMessage
    n=0
    rowIndex1 = -1
    rowIndex2 = -1
    columnIndex1 = -1
    columnIndex2 = -1
    #
    delkeyPhrase = Keyword(keyPhrase)
    keyList = Fillout(delkeyPhrase)
    messageLength = len(encodedMessage)
    while n < messageLength:
        #Step 1: wrap up a pair
        #it's always even number. So not necessary
        
        #Step 2: find the index
        #encodedMessage.index
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if ord(keyList[i][j]) == ord(encodedMessage[n]):
                    rowIndex1 = i
                    columnIndex1 = j
                if ord(keyList[i][j]) == ord(encodedMessage[n+1]):
                    rowIndex2 = i
                    columnIndex2 = j
                j += 1
            i += 1
        n += 2

        #Step 3: decode
        if rowIndex1 == rowIndex2:
            if columnIndex1 == 0:
                decodedMessage += keyList[rowIndex1][9] + keyList[rowIndex2][columnIndex2 - 1]
            elif columnIndex2 == 0:
                decodedMessage += keyList[rowIndex1][columnIndex1 - 1] + keyList[rowIndex2][9]
            else:
                decodedMessage += keyList[rowIndex1][columnIndex1 - 1] + keyList[rowIndex2][columnIndex2 - 1]
        elif columnIndex1 == columnIndex2:
            if rowIndex1 == 0:
                decodedMessage += keyList[9][columnIndex1] + keyList[rowIndex2 - 1][columnIndex2]
            elif rowIndex2 == 0:
                decodedMessage += keyList[rowIndex1 - 1][columnIndex1] + keyList[9][columnIndex2]
            else:
                decodedMessage += keyList[rowIndex1 - 1][columnIndex1] + keyList[rowIndex2 - 1][columnIndex2]                            
        else:
            decodedMessage += keyList[rowIndex1][columnIndex2] + keyList[rowIndex2][columnIndex1]

    #Step 4: remove Nul characters
    decodedMessage = decodedMessage.replace(chr(0),"")
    return decodedMessage

def encode(plainTextMessage, secretPhrase):
    matrix = Fillout(Keyword(secretPhrase))
    arr = Textforward(plainTextMessage)
    encoded = ""
    t = 0
    while t < len(arr):
        for i in range(0,10):
            for j in range(0,10):
                if arr[t] == matrix[i][j]:
                    a = i
                    b = j
        for i in range(0,10):
            for j in range(0,10):
                if arr[t+1] == matrix[i][j]:
                    c = i
                    d = j
        if a == c:
            if b == 9:
                arr[t] = matrix[a][0]
                arr[t+1] = matrix[c][d+1]
            elif d == 9:
                arr[t] = matrix[a][b+1]
                arr[t+1] = matrix[c][0]
            else:
                arr[t] = matrix[a][b+1]
                arr[t+1] = matrix[c][d+1]
        elif b == d:
            if a == 9:
                arr[t] = matrix[0][b]
                arr[t+1] = matrix[c+1][d]
            elif c == 9:
                arr[t] = matrix[a+1][b]
                arr[t+1] = matrix[0][d]
            else:
                arr[t] = matrix[a+1][b]
                arr[t+1] = matrix[c+1][d]
        else:
            arr[t] = matrix[a][d]
            arr[t+1] = matrix[c][b]
        t += 2

    for i in range(0,len(arr)):
        encoded += arr[i]
    return encoded


