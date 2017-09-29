import sys

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
        elif(nextTok=="end"):
            return
        else:
            lex()

def dec_list():
    while(nextTok != 'in'):
        dec()
        print 'test'
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
            print 'test :' 
        elif(nextTok=='='):
            match(nextTok)
            varVal = expr(varType)
            print 'test ='
            
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
    print nextTok
    return retTerm

def term(varType):
    retFact = factor(varType)
    return retFact

def factor(varType):
    retNum = nextTok
    lex()
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
if __name__=="__main__":
    main()
