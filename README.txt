# CISp2

In this project you are asked to write an interpreter which uses the top-down recursive-descent method
and inherited/synthesized attributes to parse and evaluate a very simple programming language. The tiny
strong-typed language's grammar is given below.

<Prog> := <1et-in-end> { <let-in-end> } 
<1et-in-end> = let <decl-list> in <type> ( <expr> ) end ; 
<decl-list> = <decl> { <decl> }  
<decl> = id <type> = <expr> ;  
<type> = int | real  
<expr> = <term> { + <term> | - <term> }
<term> = <factor> { * <factor> | / <factor> }
<factor> = ( <expr> ) | id | number | <type>(id)


The interpreter should be written in Python. It takes one input file which contains the program to be executed.
The input file name is given from the command line. For example,
spirit % let.py sample.tiny

The interpreter let.py reads the program file sample.tiny, checks the syntax and outputs the result for
each let-in-end if the it is legitimate; otherwise, the interpreter prints "Error". Below is a test example

Input:

let x : int = 5 ;
in
    int ( x + x * x )
end ;

let r : real = 10.0 ;
    pi : real = 3.1416
in
    real ( pi * r * r )
end ;

Output:

30
314.16

Input:

let x : int = 7
    y : real = 3.0 ;
in
    real ( ( real ( x ) + y ) * ( real ( x ) - y ) )
end;

let x = 8 ; in ( x + y ) end ;

Output:

40.0
Error
