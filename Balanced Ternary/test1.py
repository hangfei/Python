global mem
mem = ""

def divide(bt1,bt2):
    sumInt = int(bt1)/int(bt2)
    sumString = str(sumInt)
    print sumString
    sumInt = int_to_bt(sumString)
    mem = sumInt
    print "in divede",sumInt
    return sumInt

def bt_to_int(bt):
    #convert bt number to decimal
    n=0    #loop indication. to point each charater in the string
    print bt,"1 bt to int"
    stringLength = len(bt)
    dec=0    #set initial dec value
    while not stringLength == 0:
        digit = -2
        stringLength -= 1
        if bt[n] == "N":
            digit = -1
        if bt[n] == "0":
            digit = 0            
        if bt[n] == "1":
            digit = 1
        dec = dec + 3 * digit
        n += 1
    return dec


#not ok with negative!!!
def int_to_bt(dec):
    #
    bt = ""
    stringLength = len(dec)
    decNumber = int(dec)    #convert to number
    print "bt=",bt
    print dec
    while not decNumber == 0:
        #print "bt =:in loop",bt
        residual = decNumber % 3
        decNumber = decNumber /3
        #print "residual=",residual,"decNumber=",decNumber
        #print bt
        if residual == 1:
            bt ="1" + bt    #direction?
        if residual == 0:
            bt = "0" + bt
        if residual == 2:
            bt = "N" + bt
        #print "test int to bt"

    return bt

divide(1000,10)
