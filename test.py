import sys
import pdb;

tokenList = []
variableDict = {}
nextTok = None
index = -1

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
            
    variableDict[varName] = (varType,varVal)
    
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
    #Add type into term
    retTerm = term(varType)
    if(nextTok=='+'):
        match(nextTok)
        retTerm += term(varType)
    elif(nextTok=='-'):
        match(nextTok)
        retTerm -= term(varType)

    return retTerm

def term(varType):
    retFact = factor(varType)
    if(nextTok=='*'):
        match(nextTok)
        rightFact = factor(varType)
        retFact *= rightFact
    elif(nextTok=='/'):
        match(nextTok)
        retFact /= factor(varType)
    return retFact

def factor(varType):
    
    if(nextTok=='('):
        match(nextTok)
        retNum=expr(varType)
    elif(nextTok=='int' or nextTok=='real'):
        varType=type()
        #print "varType:\t",varType
        #print "nextTok:\t",nextTok
        retNum=expr(varType)
    else:
        retNum=nextTok
    if(retNum in variableDict):
        retNum = variableDict[retNum][1]
    
    lex()
    if(varType=='int'):
        return int(retNum)
    elif(varType=='real'):
        return float(retNum)
    return retNum

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
