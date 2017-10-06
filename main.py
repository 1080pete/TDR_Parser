#check to see if assigned value to variable is the correct

import sys
import pdb

tokenList = []
variableDict = {}
nextTok = None
index = -1
#swap these two below
#edit: swapped
VAL = 0
TYPE = 1


def prog():
    let_in_end()
    
def let_in_end():
    while(index < len(tokenList) - 2):
        if(nextTok=="let"):
            match(nextTok)
            dec_list()
        elif(nextTok=="in"):
            match(nextTok)
            varType = type()
            progTup = expr(varType)
            if(progTup[TYPE] == 'int'):
                final = (int(progTup[VAL]), progTup[TYPE])
            elif(progTup[TYPE] == 'real'):
                final = (float(progTup[VAL]), progTup[TYPE])
            else:
                sys.exit('ERROR1')
            print final[VAL]
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


    #Check to see if assigned type is cast right

    variableDict[varName] = (varVal[VAL], varType)
    lex() 
    return

#type check method, return type if 'int' or 'real', return error ifelse 
def type():
    if(nextTok == 'int' or nextTok == 'real'):
        returnVal = nextTok
        match(nextTok)
        return returnVal
    else:
        sys.exit('ERROR2')

def expr(varType):
    
    leftTerm = term(varType)
    total = leftTerm[VAL]
    while(True):
        #CREATE A TOTAL AND A LEFT TERM
        #check to see if there is a rightTerm and compute
       
        if(nextTok=='+'):
            match(nextTok)
            rightTerm = term(varType)
            if(leftTerm[TYPE] == rightTerm[TYPE]):
                total += rightTerm[VAL]
                varType = leftTerm[TYPE]
            else:
                sys.exit('ERROR3')
            
        elif(nextTok=='-'):
            match(nextTok)
            rightTerm = term(varType)
            if(leftTerm[TYPE] == rightTerm[TYPE]):
                total -= rightTerm[VAL]
                varType = leftTerm[TYPE]
            else:
                sys.exit('ERROR4')
        
        #FIX THIS
        elif(nextTok == ')' or nextTok == ';' or nextTok == 'end'):
            break

    finalTup = (total, varType)
    return finalTup

def term(varType):
    
    leftFact = factor(varType)
    total = leftFact[VAL]

    while(True):
   
    #check to see if there is a rightFact and compute
        if(nextTok=='*'):
            match(nextTok)
            rightFact = factor(varType)
            if(leftFact[TYPE] == rightFact[TYPE]):
                total *= rightFact[VAL] 
                varType = rightFact[TYPE]
            else:
                sys.exit('ERROR5')

        elif(nextTok=='/'):
            match(nextTok)
            rightFact = factor(varType)
            if(leftFact[TYPE] == rightFact[TYPE]):
                total /= rightFact[VAL] 
                varType = rightFact[TYPE]
            else:
                sys.exit('ERROR6')
        else:
            break
    finalFact = (total, varType)
    return finalFact

def factor(varType):
    
    #initialize retTup 
    retTup = ()

    #check to see if nextTok is paranthesis or variable type
    if(nextTok=='('):
        match(nextTok)
        exprVal = expr(varType)
        retTup = (exprVal[VAL], varType)
        match(')')

   
        
    elif(nextTok=='int' or nextTok=='real'):
        varType=type()
        if(nextTok=='('):
            match(nextTok)
            value = varDef(nextTok, varType)
            match(nextTok)
            retTup = (value, varType)
            match(')')
    else:
        '''old
        value = varDef(nextTok, varType)
        retTup = (value, varType)
        '''
        #NEW
        value = varDef(nextTok, varType)
        retTup = value
        lex()
    

    #if factor has a stored value, convert value and return value and varType
  
    
    #New:
    
    return retTup
#match to see if nextTok is correct, if not print error
def match(token):
    if(token==nextTok):
        lex()
    else:
        print token
        sys.exit('ERROR7')
         

#update nextTok and index counter
def lex():
    global index, nextTok

    index += 1
    nextTok = tokenList[index]

def arith(left, tok, right):
    if(left[TYPE] == right[TYPE]):
        if(tok == '+'):
            match(tok)
            print left[VAL]
            print right[VAL]
            return (left[VAL] + right[VAL])
        elif(tok == '-'):
            match(tok)
            return left - right
        elif(tok == '*'):
            match(tok)
            return left - right
        elif(tok == '/'):
            match(tok)
            return left / right
        else:
            sys.exit('ERROR arit')
    else:
        sys.exit('ERROR arith match')

def varDef(variable, varType):
    
    varNum = 0
    if variable in variableDict:
        varNum = variableDict[variable]
        return varNum
    else:
        if varType == 'int':
            try:
                varNum = int(variable)
                return varNum
            except(ValueError):
                sys.exit('ERROR int')
        elif varType == 'real':
            try:
                varNum = float(variable)
                return varNum
            except(ValueError):
                sys.exit('ERROR float')
            
#initialze program
def main():
    global tokenList
    file = open('test1.txt','r')
    tokenList = file.read().split()
    lex()
    prog()


if __name__=="__main__":
    main()