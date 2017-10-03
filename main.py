import sys
import pdb

tokenList = []
variableDict = {}
nextTok = None
index = -1
TYPE = 0
VAL = 1

def prog():
        let_in_end()
    
def let_in_end():
    while(index < len(tokenList) - 2):
        if(nextTok=="let"):
            match(nextTok)
            dec_list()
        elif(nextTok=="in"):
            match(nextTok)
            final = expr(type())
            print final
        elif(nextTok=="end"):
            return
        else:
            lex()

def dec_list():
    while(nextTok != 'in'):
        dec()
    return

#
def dec():
    global variableDict
    varType,varVal = None,None
    varName = nextTok

    lex()

    #read through declerations and insert them into variableDict with VAL and varType
    while(nextTok != ';'):
        if(nextTok==':'):
            match(nextTok)
            varType = type()
        elif(nextTok=='='):
            match(nextTok)
            varVal = expr(varType)
            
    variableDict[varName] = (varType,varVal[VAL])
    
    lex() 
    return

#type check method, return type if 'int' or 'real', return error ifelse 
def type():
    if(nextTok == 'int' or 'real'):
        returnVal = nextTok
        match(nextTok)
        return returnVal
    else:
        sys.exit('Error')

def expr(varType):
    #initialize leftTerm
    leftTerm = term(varType)

    #check to see if there is a rightTerm and compute
    if(nextTok=='+'):
        match(nextTok)
        rightTerm = term(varType)
        finalTerm = (varType, (leftTerm[VAL] + rightTerm[VAL]))
        return finalTerm
    elif(nextTok=='-'):
        match(nextTok)
        rightTerm = term(varType)
        finalTerm = (varType, (leftTerm[VAL] - rightTerm[VAL]))
        return finalTerm

    return leftTerm

def term(varType):
    #initialize leftFact
    leftFact = factor(varType)

    #check to see if there is a rightFact and compute
    if(nextTok=='*'):
        match(nextTok)
        rightFact = factor(varType)
        finalFact = (varType, (leftFact[VAL] * rightFact[VAL]))
        return finalFact
    elif(nextTok=='/'):
        match(nextTok)
        rightFact = factor(varType)
        finalFact = (varType, (leftFact[VAL] / rightFact[VAL]))
        return finalFact

    return leftFact

def factor(varType):
    #initialize retTup 
    retTup = ()

    #check to see if nextTok is paranthesis or variable type
    if(nextTok=='('):
        match(nextTok)
        exprCheck = expr(varType)
        retTup = (varType, exprCheck[1])
    elif(nextTok=='int' or nextTok=='real'):
        varType=type()
        if(nextTok=='('):
            match(nextTok)
            exprCheck = expr(varType) 
            retTup = (varType, exprCheck[1])
    else:
        retTup = (varType, nextTok)
    lex()

    #if factor has a stored value, convert value and return value and varType
    if(retTup[TYPE]=='int'):
        if(retTup[VAL] in variableDict):
            finalTup = (varType, int(variableDict[retTup[VAL]][VAL]))
            print finalTup
            return finalTup
    elif(retTup[TYPE]=='real'):
        if(retTup[VAL] in variableDict):
            finalTup = (varType, float(variableDict[retTup[VAL]][VAL]))
            return finalTup

    return retTup

#match to see if nextTok is correct, if not print error
def match(token):
    if(token==nextTok):
        lex()
    else:
        sys.exit('Error')

#update nextTok and index counter
def lex():
    global index, nextTok

    index += 1
    nextTok = tokenList[index]

#initialze program
def main():
    global tokenList
    file = open('test.txt','r')
    tokenList = file.read().split()
    lex()
    prog()
    print variableDict
if __name__=="__main__":
    main()
