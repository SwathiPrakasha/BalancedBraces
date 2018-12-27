#!/bin/python3

"""
This function handles multiple string passed to the function. 
TIme Complexity level O(n2)
 
"""
def checkBraces(inputData):
    res = []
    for st in inputData:
        stack =[]
        closeBeforeOpen = False

        for brace in st:
            if brace == '(' or brace == '[' or brace =='{':
                stack.append(brace)

            if len(stack) == 0:
                closeBeforeOpen = True
                break

            elif brace == ')':
                x = stack.pop()
                if x == '[' or x == '{':
                    break
                
            elif brace == ']':
                x = stack.pop()
                if x == '(' or x == '{':
                    break
                
            elif brace == '}':
                x = stack.pop()
                if x == '(' or x == '[':
                    break
                
        if len(stack) !=0:
            res.append('NO')
        elif closeBeforeOpen == True:
            res.append('NO')
        else:
            res.append('YES')
    
    return res
        
#print(checkBraces(['[](){()}']))
#print(checkBraces(['([)])']))
print(checkBraces(['}][}}(}][))]', '[](){()}', '()', '({}([][]))[]()','{)[](}]}]}))}(())(','([[)']))
