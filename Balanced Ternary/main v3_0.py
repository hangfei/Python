
#global variable mem
global mem
mem="0"




#basically done
def bt_to_int(bt):
    #convert bt number to decimal
    n=0    #loop indication. to point each charater in the string
    stringLength = len(bt)
    dec=0    #set initial dec value
    #revised this while from v1.0
    while n < stringLength :
        digit = -2       
        if bt[stringLength - n - 1] == "N":
            digit = -1
        if bt[stringLength - n - 1] == "0":
            digit = 0            
        if bt[stringLength - n - 1] == "1":
            digit = 1
        dec = dec + (3 ** n) * digit
        n += 1
    return dec




#not ok with negative!!!
#code be omiited....by mistake
#basically done
def int_to_bt(dec):
    #add dec == "0" conditioanl
    if dec == "0":
        return dec    
    bt = ""
    stringLength = len(dec)
    decNumber = int(dec)    #convert to number
    while not decNumber == 0:
        residual = decNumber % 3
        decNumber = decNumber /3
        if residual == 1:
            bt ="1" + bt    #direction?
        if residual == 0:
            bt = "0" + bt
        if residual == 2:
            bt = "N" + bt
            decNumber += 1
    return bt


#functions
def add(bt1,bt2):
    bt1Int = bt_to_int(bt1)
    bt2Int = bt_to_int(bt2)
    resultInt = int(bt1Int)+int(bt2Int)
    resultString = str(resultInt)
    resultBt = int_to_bt(resultString)
    store(resultBt)
    return resultBt

def subtract(bt1,bt2):
    bt1Int = bt_to_int(bt1)
    bt2Int = bt_to_int(bt2)
    resultInt = int(bt1Int) - int(bt2Int)
    resultString = str(resultInt)
    resultBt = int_to_bt(resultString)
    store(resultBt)
    return resultBt

def multiply(bt1,bt2):
    bt1Int = bt_to_int(bt1)
    bt2Int = bt_to_int(bt2)
    resultInt = int(bt1Int) * int(bt2Int)
    resultString = str(resultInt)
    resultBt = int_to_bt(resultString)
    store(resultBt)
    return resultBt 

def divide(bt1,bt2):
    bt1Int = bt_to_int(bt1)
    bt2Int = bt_to_int(bt2)
    resultInt = int(bt1Int) / int(bt2Int)
    resultString = str(resultInt)
    resultBt = int_to_bt(resultString)
    store(resultBt)
    return resultBt

def remainder(bt1,bt2):
    bt1Int = bt_to_int(bt1)
    bt2Int = bt_to_int(bt2)
    resultInt = int(bt1Int) % int(bt2Int)
    resultString = str(resultInt)
    resultBt = int_to_bt(resultString)
    store(resultBt)
    return resultBt

def negate(bt1):
    bt1Int = bt_to_int(bt1)
    resultInt = - int(bt1Int)
    resultString = str(resultInt)
    resultBt = int_to_bt(resultString)
    store(resultBt)
    return resultBt

#--------
def store(bt):
    global mem
    mem = bt
    if mem == bt:
        return True
    else:
        return False

def fetch():
    global mem
    return mem


#--------

def evaluate(string):

    #--------
    #Step 0!
    #if operator is "-1", means errors
    operand1 = ""
    operand2 = ""
    operator = ""
    #this should be put after tackling mem
    #stringLength = len(string)

    #tackle mem
    while "mem" in string:
        t = fetch()
        string=string.replace("mem",t)
        print "OK"
        print string
        

    #--------
    #Step 1!
    #check for illegal characters
    stringLength = len(string)
    n = -1
    while n < stringLength -1 :
        n += 1
        if string[n] not in "1234567890N dec bt + - * / %":
            operator = "-1"
            print "Error1!"
            return "Invalid input: other characters and numbers."
            break

    #--------
    #Step 2!
    #
    #string[0:3] represents start from 0 to the next 3  charaters
    #use operator as indication to separate the three loops
    ##!!!better?:every time satisfies the contional, let it go into a smaller loop
    n = -1
    while  n < stringLength-1 and operator != "-1":
        #put n at the start
        n += 1

        #better to set operand1 if there is no operand1 after loop
        if (string[n] == "N" or string[n] == "0" or string[n] == "1") and operator == "":            
            operand1 +=string[n]
            #print n,string[n]
            continue

        #why use continue? Or the third loop will be excuted even operator
        #is not finished
        #use operand2 == ""

        if (string[n] != "N" and string[n] != "0" and string[n] != "1" and string[n] != " " and string[n] not in "1234567890") and operand2 == "":
            operator = operator + string[n]
            if operator == "bt":
                if string[n+1] == " ":
                    if string[n+2] == "-":
                        operand2 = "-"
                        n = n + 2
                elif string[n+1] == "-":
                    operand2 = "-"
                    n += 1
            print "loop2",operand2
            print operator
            continue
            
            
        #if the first one is space, it would be wrong.
        #Solved by adding operator != ''. ensure the operator process is finished

        #to be strict, we can let operator only equals the given strings
        if operator != '':
            #print "loop3"
            if string[n] != " " and operator != "bt" and (string[n] == 'N' or string[n] == "1" or string[n] == "0"):
                operand2 = operand2 + string[n]
            if operator == "bt" and (string[n] in "1234567890-"):
                operand2 = operand2 + string[n]

    print "Start!"
    print operand1
    print operator
    print operand2
    print "Finish!"
    print
    print
    #quit?


    #--------
    #Step 3!
    #
    #Checks for problems
    #check program should be put behind the split program
    if operator not in "'+','-','*','/','%'" and operator != "dec" and operator != "bt":
        print operator
        print "Error2!"
        return False
    if operator == "bt":
        n = -1
        while n < len(operand2)-1:
            n += 1
            if operand2[n] not in "1234567890-":
                print "Error3!"
                return False
        
    else:
        while n < len(operand1):
            if operand1[n] not in "N01":
                print "Error4!"
                return False
        while n < len(operand2):
            if operand2[n] not in "N01":
                print "Error5!"
                return False


    #???
    if operand2 == "0" and (operator == "/" or operator == "%"):
        print "Error! (Division or mod by zero)"



    #--------
    #Step 4!
    #
    #Calls one of the above methods to perform the arithmetic,
    #and return the result as a string.
    #add a numberofOperand

    #if needed, convert to decimal
    #should put in each functions or in func evaluate?
    #not useful in v3.0
    if operator != "bt":
        operand1Int = bt_to_int(operand1)
        operand2Int = bt_to_int(operand2)
        

    #Situation 1
    #two operands
    if  operand1 != "":
        if operator == "+":
            add(operand1,operand2)
            
        if operator == "-":
            return subtract(operand1,operand2)
            
        #need to exclude zero
        if operator == "/":
            return divide(operand1,operand2)

        if operator == "*":
            return multiply(operand1,operand2)

        if operator == "%":
            return remainder(operand1,operand2)
        


    #Situation 2
    #one operand
    else:
        if operator == "-":
            t = negate(operand2)
            store(t)
            return negate(operand2)
            
        if operator == "dec":
            return bt_to_int(operand2)
 
        if operator == "bt":
            t = int_to_bt(operand2)
            store(t)
            return int_to_bt(operand2)   

#mem = "NNNNNNNNNNNNNNNNNN"
#evaluate("mem + NN!1N")
#evaluate("-NaNN")
#evaluate("dec NNNN")
#evaluate("dafkj;23")
#evaluate("+ NNNN + 0001")
#!!!
#s=evaluate("dec NNNNN")
#print s


def REPL():

    #--------
    #Step 0!
    print "Please input.(Input quit to exit.)"
    print

    #--------
    #Step
    userInput   = ""
    while userInput != "quit":
        userInput = raw_input("Compute: ")
        if userInput == "quit":
            return
        print userInput
        userOutput = evaluate(userInput)
        
        print userOutput
        print "mem=",mem


if __name__ == '__main__':
        print "1main"
        REPL()
