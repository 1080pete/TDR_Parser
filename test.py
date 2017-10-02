import sys
import pdb;

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

def dec():
    global variableDict
    varType,varVal = None,None
    varName = nextTok

    lex()
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


def type():
    if(nextTok == 'int' or 'real'):
        returnVal = nextTok
        match(nextTok)
        return returnVal
    else:
        sys.exit('Error')

def expr(varType):
    leftTerm = term(varType)

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
    #print 'before:\t\t\t',nextTok
    leftFact = factor(varType)
    #print 'after:\t\t\t',nextTok
    #print leftFact
    if(nextTok=='*'):
        match(nextTok)
        rightFact = factor(varType)
        #print rightFact
        #print leftFact
        finalFact = (varType, (leftFact[VAL] * rightFact[VAL]))
        return finalFact
    elif(nextTok=='/'):
        match(nextTok)
        rightFact = factor(varType)
        finalFact = (varType, (leftFact[VAL] / rightFact[VAL]))
        return finalFact

    return leftFact

def factor(varType):
    exprCheck = None
    retTup = ()
    if(nextTok=='('):
        match(nextTok)
        exprCheck = expr(varType)
        retTup = (varType, exprCheck[1])
    elif(nextTok=='int' or nextTok=='real'):
        varType=type()
        exprCheck = expr(varType) 
        retTup = (varType, exprCheck)
    else:
        retTup = (varType, nextTok)
    lex()

    if(exprCheck[0] in variableDict):
        if(retTup[TYPE]=='int'):
            finalTup = (varType, int(variableDict[retTup[VAL]][VAL]))
            print finalTup
            return finalTup
        elif(retTup[TYPE]=='real'):
            finalTup = (varType, float(variableDict[retTup[VAL]][VAL]))
            return finalTup
    return retTup

def match(token):
    if(token==nextTok):
        lex()
    else:
        sys.exit('Error')


def lex():
    global index, nextTok

    index += 1
    nextTok = tokenList[index]

def main():
    global tokenList
    file = open(sys.argv[1],'r')
    tokenList = file.read().split()
    lex()
    prog()
    print variableDict
if __name__=="__main__":
    main()