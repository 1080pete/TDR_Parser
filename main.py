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
	dec()

def dec():
	global varDict
	
	varType,varVal = None,None
	var = nextTok

	match(nextTok)
	if(nextTok ==":"):
		match(nextTok)
		varType = type()
	print varType
	if(nextTok=="="):
		print "test"
		match(nextTok)

def type():
	tok = tokList[index]
	
	if(tok=="int" or tok=="real"):
		lex()
		return tok
	else:
		return -1	

def expr():
	


	
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
	
			
if __name__=="__main__":
	main()
