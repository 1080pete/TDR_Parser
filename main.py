#create global variable for count
#create global dict? read in as id then change based on func


import sys

tokIndex = -1
nextTok = None
tokList = []
varDict = {}

def prog():
    lex()
    letInEnd()

def letInEnd():
    varTypeCheck = None

    while(tokIndex < len(tokList)-2):
	if(nextTok == "let"):
		match(nextTok)
		decList()
	elif(nextTok == "in"):
		match(nextTok)
		varTypeCheck = type()
                #print varTypeCheck
	else:
		lex()		
			
def decList():
    while (nextTok != "in"):
        dec()
    return

def dec():
    global varDict	
    varType,varVal = None,None
    var = nextTok

    match(nextTok)
    if(nextTok ==":"):
	match(nextTok)
	varType = type()
        match(nextTok)
        varVal = expr()
        varDict[var] = (varType,varVal)

def type():
    tok = tokList[tokIndex]
	
    if(tok=="int" or tok=="real"):
        match(tok)	
	return tok
    else:
        sys.exit('Error')

def expr():
    leftTerm = float(term())
    rightTerm = None
    print "leftTerm:\t",leftTerm
    print "nextTok:\t",nextTok
    if(nextTok=="+"):
        match(nextTok)
        rightTerm = term()
        leftTerm += float(rightTerm)
        return leftTerm
    elif(nextTok=="-"):
        match(nextTok)
        leftTerm += term()
        return leftTerm
    else:
        return leftTerm


def term():
    leftFactor = factor()
    
    match(nextTok)
    if(nextTok=="*"):
        match(nextTok)
        leftFactor *= factor()
    elif(nextTok=="/"):
        match(nextTok)
        leftFactor /= factor()
    else:
        return leftFactor



def factor():
    if(nextTok in varDict):
        return varDict[nextTok][1]
    else:
        return nextTok


	
def lex():
	global tokIndex, nextTok
	tokIndex+=1
	nextTok = tokList[tokIndex]

def match(token):
    if (nextTok == token):
    	lex()
    else:
	sys.exit('Error')
	
def read():
    global tokList

    file = open(sys.argv[1],"r")
    tokList = file.read().split()
	
	
	
def main():
    read()
    prog()
    print varDict	
			
if __name__=="__main__":
    main()
