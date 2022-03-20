# Problem Statement
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
#
# Code
def valid_parentheses(string):
    open = 0
    closed = 0
    for ele in string:
        if open>=closed:
            if ele == "(":
                open+=1
            elif ele == ")":
                closed+=1
        else:
            return False
    if open-closed == 0:
        return True
    else:
        return False
