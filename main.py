#create global variable for count
#create global dict? read in as id then change based on func


import sys
count = 0
list = []

'''
class lex():

class match(token)	
	if(
prog(){
}
letInEnd(){
}
declList(){
}
decl(){
}
type(){
}
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
def match():
	global count
	count += 1
def read():
	file = open(sys.argv[1],"r")
	global list
	list = file.read().split()

read()
for v in list:
	print list[count]
	match()
				

