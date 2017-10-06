import sys
import pdb

tokenList = []
variableDict = {}
nextTok = None
index = -1
VAL = 0
TYPE = 1

def prog():
    let_in_end()
    
def let_in_end():
    while index < len(tokenList) - 2:
        if nextTok == "let":
            match(nextTok)
            dec_list()
        elif nextTok == "in":
            match(nextTok)
            varType = type()
            progTup = expr(varType)

            if progTup[TYPE] == 'int':
                final = (int(progTup[VAL]), progTup[TYPE])
            elif progTup[TYPE] == 'real':
                final = (float(progTup[VAL]), progTup[TYPE])
            else:
                sys.exit('ERROR:\t WRONG VAL ASSIGNMENT')
            print final[VAL]
        else:
            lex()

def dec_list():
    while nextTok != 'in':
        dec()
    return

def dec():
    global variableDict
    varType, varVal = None, None
    varName = nextTok

    #read through declerations and insert them into variableDict with VAL and varType
    lex()
    if nextTok == ':':
        match(nextTok)
        varType = type()
        if nextTok == '=':
            match(nextTok)
            varVal = expr(varType)
            match(';')
        else:
            sys.exit('ERROR:\tWRONG DECLERATION FORMAT')
    else:
        sys.exit('ERROR:\tWRONG DECLERATION FORMAT')

    variableDict[varName] = (varVal[VAL], varType)
    return

#type check method, return type if 'int' or 'real', return error ifelse
def type():
    if nextTok == 'int' or nextTok == 'real':
        returnVal = nextTok
        match(nextTok)
        return returnVal
    else:
        sys.exit('ERROR:\tWRONG TYPE')

def expr(varType):
    leftTerm = term(varType)
    total = leftTerm[VAL]

    while(True):
        #CREATE A TOTAL AND A LEFT TERM
        #check to see if there is a rightTerm and compute    
        if nextTok == '+':
            match(nextTok)
            rightTerm = term(varType)
            leftNew = (total, leftTerm[TYPE])
            total = arith(leftNew, '+', rightTerm)
            varType = leftTerm[TYPE]
        elif nextTok == '-':
            match(nextTok)
            rightTerm = term(varType)
            leftNew = (total, leftTerm[TYPE])
            total = arith(leftNew, '-', rightTerm)
            varType = leftTerm[TYPE]
        elif nextTok == ')' or nextTok == ';' or nextTok == 'end':
            break
        else:
            sys.exit('ERROR:\tEXPRESION ERROR')

    finalTup = (total, varType)
    return finalTup

def term(varType):
    leftFact = factor(varType)
    total = leftFact[VAL]

    while True:
    #check to see if there is a rightFact and compute
        if nextTok == '*':
            match(nextTok)
            rightFact = factor(varType)
            leftNew = (total, leftFact[TYPE])
            total = arith(leftNew, '*', rightFact)
            varType = leftFact[TYPE]
        elif nextTok == '/':
            match(nextTok)
            rightFact = factor(varType)
            leftNew = (total, leftFact[TYPE])
            total = arith(leftNew, '/', rightFact)
            varType = leftFact[TYPE]
        else:
            break
    finalFact = (total, leftFact[TYPE])
    return finalFact

def factor(varType):
    retTup = ()
    #check to see if nextTok is paranthesis or variable type
    if nextTok == '(':
        match(nextTok)
        exprVal = expr(varType)
        retTup = (exprVal[VAL], varType)
        match(')')
    elif nextTok == 'int' or nextTok == 'real':
        varType=type()
        if nextTok == '(':
            match(nextTok)
            value = varDef(nextTok, varType)
            match(nextTok)
            retTup = (value[VAL], varType)
            match(')')
    else:
        value = varDef(nextTok, varType)
        retTup = value
        lex()
    return retTup

#match to see if nextTok is correct, if not print error
def match(token):
    if(token==nextTok):
        lex()
    else:
        print token
        sys.exit('ERROR:\tMATCH ERROR')

#update nextTok and index counter
def lex():
    global index, nextTok
    index += 1
    nextTok = tokenList[index]

def arith(left, operation, right):
    returnVal = 0
    if left[TYPE] == right[TYPE]:
        if operation == '+':
            returnVal = left[VAL] + right[VAL]
            return returnVal
        elif operation == '-':
            returnVal = left[VAL] - right[VAL]
            return returnVal
        elif operation == '*':
            returnVal = left[VAL] * right[VAL]
            return returnVal
        elif operation == '/':
            returnVal = left[VAL] / right[VAL]
            return returnVal
        else:
            sys.exit('ERROR:\tINVALID OPERATION')
    else:
        sys.exit('ERROR:\tTYPE MATCH INVALID')

def varDef(variable, varType): 
    varNum = 0
    if variable in variableDict:
        varNum = variableDict[variable]
        return varNum
    else:
        if varType == 'int':
            try:
                varNum = (int(variable), varType)
                return varNum
            except(ValueError):
                sys.exit('ERROR:\tCANNOT CAST INT')
        elif varType == 'real':
            try:
                varNum = (float(variable), varType)
                return varNum
            except(ValueError):
                sys.exit('ERROR:\tCANNOT CAST FLOAT')
            
#initialze program and read file into global list, lex() into nextTok and execute prog()
def main():
    global tokenList
    file = open('test1.txt','r')
    tokenList = file.read().split()
    lex()
    prog()

if __name__=="__main__":
    main()