from collections import deque
def Balanced_Parenthesis(s):
    stack=deque()
    d={'(':')','{':'}','[':']'}
    for i in s:
        if i in d:
            stack.append(i)
            print(stack)
        else:
            if not stack:
                return False
            if i!=d[stack.pop()]:
                return False
            
    if stack:
        return False
    return True

s='({[]}())()'
print(Balanced_Parenthesis(s))

        