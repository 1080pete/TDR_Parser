#create global variable for count
#create global dict? read in as id then change based on func


import sys
count = 0
tokList = []

'''
class lex():

class match(token)	
	if(
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
def prog():
	letInEnd()




def match():
	global count
	count += 1
def read():
	file = open(sys.argv[1],"r")
	global tokList
	tokList = file.read().split()
def main():

	global tokList
	read()
	
	for v in tokList:
		print tokList[count]
		match()
				
if __name__=="__main__":
	main()
