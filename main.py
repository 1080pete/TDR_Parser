#create global variable for count
#create global dict? read in as id then change based on func


import sys
from IPython import embed

index = -1
nextTok = None
tokList = []
varDict = {}

'''

expr(){
}
term(){
}
factor(){
}

factor(){
	lex();
	if(nextToken=="id"){
	}
	elif
}

'''
def prog():
    lex()
    letInEnd()

def letInEnd():
    while(index < len(tokList)-2):
	if(nextTok == "let"):
		match(nextTok)
		decList()
	elif(nextTok == "in"):
		match(nextTok)
		#type()
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
        varVal = expr()
        #print "varType\t",varType
        #print "varVal\t",varVal
        varDict[var] = (varType,varVal)

def type():
    tok = tokList[index]
	
    if(tok=="int" or tok=="real"):
        match(tok)	
	return tok
    else:
    	return -1	

def expr():
    retExpr = term()
    print nextTok
    return retExpr


def term():
    retTerm = factor()
    return retTerm

def factor():
    lex()
    return nextTok


	
def lex():
	global index, nextTok
	index+=1
	nextTok = tokList[index]

def match(token):
    if (nextTok == token):
    	lex()
    else:
	return -1
	
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
