'''
#old
def let_in_end():
    #loop through tokenList until last token is read
    while index < len(tokenList) - 2:
        if nextTok == "let":
            match(nextTok)
            dec_list()
        elif nextTok == "in":
            match(nextTok)
            varType = type()
            progList = expr(varType)

            if progList[TYPE] == 'int':
                final = (int(progList[VAL]), progList[TYPE])
            elif progList[TYPE] == 'real':
                final = (float(progList[VAL]), progList[TYPE])
            else:
                sys.exit('ERROR:\t WRONG VAL ASSIGNMENT')
            print final[VAL]
        else:
            lex()
'''
#new

def let_in_end():
    match('let')
    dec_list()
    match('in')
    varType = type()
    progList = expr(varType)
    match('end')
    if nextTok == ';'
        return
    else:
        sys.exit('ERROR')