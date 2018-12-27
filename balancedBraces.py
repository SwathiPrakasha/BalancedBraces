#!/bin/python3
"""
This function handles only one input at a time. 
TIme Complexity level O(n)
 
"""
def checkBraces(str1):
    stack =[]

    for brace in str1:
        
        if brace == '(' or brace == '[' or brace =='}':
             stack.append(brace)

        if len(stack) == 0:
            return False

        elif brace == ')':
            x = stack.pop()
            if x == '[' or x == '{':
                return False
            
        elif brace == ']':
            x = stack.pop()
            if x == '(' or x == '{':
                return False
            
        elif brace == '}':
            x = stack.pop()
            if x == '(' or x == '[':
                return False
            
    if (len(stack) ==0):
        return True
    else:
        return False
    

print(checkBraces('({})'))
print(checkBraces('([)])'))
