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

#DEC CHANGED TO LIST
def let_in_end():
    while index < len(tokenList) - 2:
        if nextTok == "let":
            match(nextTok)
            dec_list()
        elif nextTok == "in":
            match(nextTok)
            varType = type()
            progList = expr(varType)

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

#DEC FINE
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

#EXPR DONE
def expr(varType):
    leftTerm = term(varType)

    while(True):
        #CREATE A TOTAL AND A LEFT TERM
        #check to see if there is a rightTerm and compute    
        if nextTok == '+':
            match(nextTok)
            rightTerm = term(varType)
            leftTerm[VAL] = arith(leftTerm, '+', rightTerm)
        elif nextTok == '-':
            match(nextTok)
            rightTerm = term(varType)
            leftTerm[VAL] = arith(leftTerm, '-', rightTerm)
        elif nextTok == ')' or nextTok == ';' or nextTok == 'end':
            break
        else:
            sys.exit('ERROR:\tEXPRESION ERROR')

    return leftTerm

#TERM DONE
def term(varType):
    leftFact = factor(varType)

    while True:
    #check to see if there is a rightFact and compute
        if nextTok == '*':
            match(nextTok)
            rightFact = factor(varType)
            leftFact[VAL] = arith(leftFact, '*', rightFact)
        elif nextTok == '/':
            match(nextTok)
            rightFact = factor(varType)
            leftFact[VAL] = arith(leftFact, '/', rightFact)
        else:
            break
    return leftFact

#FACTOR DONE
def factor(varType):
    retList = []
    #check to see if nextTok is paranthesis or variable type
    if nextTok == '(':
        match(nextTok)
        exprVal = expr(varType)
        retList = [exprVal[VAL], varType]
        match(')')
    elif nextTok == 'int' or nextTok == 'real':
        varType=type()
        if nextTok == '(':
            match(nextTok)
            value = varDef(nextTok, varType)
            match(nextTok)
            retList = [value[VAL], varType]
            match(')')
    else:
        retList = varDef(nextTok, varType)
        lex()
    return retList

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

#ARITH DONE
def arith(left, operation, right):
    rightNum = right[VAL]
    print 'rightNum:\t', rightNum
    print 'leftNum:\t', left[VAL]
    if left[TYPE] == right[TYPE]:
        if operation == '+':
            left[VAL] += rightNum
            return left
        elif operation == '-':
            left[VAL] -= rightNum
            return left
        elif operation == '*':
            left[VAL] *= rightNum
            return left
        elif operation == '/':
            left[VAL] /= rightNum
            return left
        else:
            sys.exit('ERROR:\tINVALID OPERATION')
    else:
        sys.exit('ERROR:\tTYPE MATCH INVALID')


def varDef(variable, varType): 
    if variable in variableDict:
        varList = list(variableDict[variable])
        return varList
    else:
        if varType == 'int':
            try:
                varList = [int(variable), varType]
                return varList
            except(ValueError):
                sys.exit('ERROR:\tCANNOT CAST INT')
        elif varType == 'real':
            try:
                varList = [float(variable), varType]
                return varList
            except(ValueError):
                sys.exit('ERROR:\tCANNOT CAST FLOAT')
#initialze program and read file into global list, lex() into nextTok and execute prog()
def main():
    global tokenList
    file = open('test.txt','r')
    tokenList = file.read().split()
    lex()
    prog()

if __name__=="__main__":
    main()