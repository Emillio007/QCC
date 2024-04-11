from show import *
from showcq import *
from helpers import *
from PEjames import *
from lark import *

#Declaration parser
dp = Lark.open("QCC/CQ-python/CQ.lark", start="declaration")
#Statement parser
sp = Lark.open("QCC/CQ-python/CQ.lark", start="statement")
#Full program parser
pp = Lark.open("QCC/CQ-python/CQ.lark", parser="lalr", start="program")

"""The four different declaration types: uninit variable, init variable, uninit array, init array"""
decl0 = dp.parse("int a;")
decl1 = dp.parse("int b = 12;")
decl2 = dp.parse("int c[4];")
decl3 = dp.parse("int d[3] = {1, 2, 3};")

declarations = {decl0, decl1, decl2, decl3}

"""The different statement types: """
#variable assigment
#qupdate
#qupdate if bool
#procedure call (function call?)
#measure qbit -> cbit
#if(bool_exp) do_statement else do_other_statement
#while(bool_exp) do_statement
#block
statements = {
    sp.parse("a = 3;"),
    sp.parse("not q[0];"),
    sp.parse("not q[0] if c[0];"),
    sp.parse("call my_function(a, b, c);"),
    sp.parse("measure q[0] -> c[0];"),
    sp.parse("if(bv == true){a = 4;}else{a = 5;}"),
    sp.parse("while(a < 10){not q[0];}"),
    sp.parse("{a = 1;}")
}

#Read full qft2.cq program:
f = open("QCC/CQ-programs/qft2.cq", 'r')
qft2 = pp.parse(f.read(), start="program")

def decls():
    for decl in declarations:
        print(show_declaration(decl))

def stats():
    for stat in statements:
        print(show_statement(stat))

def prog():
    #Is qft2 well-typed?
    type_program(qft2)
    print(showcq_program(qft2))

def PE_prog():
    #Partially evaluate qft2:
    print(show_program(PE_program(qft2, static_input={})))

"""
Run tests:
"""

def main():
    #decls()
    #stats()
    #prog()
    PE_prog()

if __name__ == "__main__":
    main()