'''Infix expressions are readable and solvable by humans. We can easily distinguish the order of operators, 
and also can use the parenthesis to solve that part first during solving mathematical expressions. 
The computer cannot differentiate the operators and parenthesis easily, that’s why postfix/prefix conversion is needed.
Compilers or command editor in computer and some calculators also convert expression to prefix/postfix first and 
then solve those expression to evaluate answer for the same.

scan from let to right 
1. if oprant/variable come then print
2. if ( bracket come then push to stack 
3. if operator come then push if no oprator on top of stack
   if top of stack has operator then check precedence of operator is higher than operator on top of stack 
   then push it to stack 
   If the precedence of the operator is lower than or equal to the precedence of the top of the stack, 
   pop the operators from the stack and output them to the postfix expression 
   until a lower precedence operator is encountered or the stack becomes empty. 
   Then, push the operator onto the stack.
4. If the scanned element is a closing parenthesis ')', pop operators from the stack until ( incounter
5. after expression end pop until stack empty and show'''


from collections import deque
def Postfix(s):
    precedence={'+':1,'-':1,'*':2,'/':2}
    ans=''
    stack=deque()
    for i in s:
        if i.isalnum():
            ans+=i
            continue
        if i=='(':
            stack.append(i)
        elif i in precedence:
            if stack:
                    while stack and stack[-1]!='('and precedence[i]<=precedence[stack[-1]]:
                        ans+=stack.pop()
                    stack.append(i)
            else:
                stack.append(i)
        else:
            while stack and stack[-1]!='(':
                ans+=stack.pop()
    while stack:
        k=stack.pop()
        if k!='(':
            ans+=k
    return ans

'''scan from right to left.
1. if oprant/variable come then print
2. if ) bracket come then push to stack 
3. if operator come then push if no oprator on top of stack
   if top of stack has operator then check precedence of operator is higher than operator on top of stack 
   then push it to stack 
   If the precedence of the operator is lower than or equal to the precedence of the top of the stack, 
   pop the operators from the stack and output them to the postfix expression 
   until a lower precedence operator is encountered or the stack becomes empty. 
   Then, push the operator onto the stack.
4. If the scanned element is a closing parenthesis '(', pop operators from the stack until ) incounter
5. after expression end pop until stack empty and show
6 at last reverse the result'''   
def Prefix(s):
    precedence={'+':1,'-':1,'*':2,'/':2}
    ans=''
    stack=deque()
    for i in s:
        if i.isalnum():
            ans+=i
            continue
        if i==')':
            stack.append(i)
        elif i in precedence:
            if stack:
                    while stack and stack[-1]!=')'and precedence[i]<=precedence[stack[-1]]:
                        ans+=stack.pop()
                    stack.append(i)
            else:
                stack.append(i)
        else:
            while stack and stack[-1]!=')':
                ans+=stack.pop()
    while stack:
        k=stack.pop()
        if k!=')':
            ans+=k
    ans=''.join(reversed(ans))
    return ans



s='a+(b/c)'
s1='(a+b)*c'
s3='(a+b)*(c+d)'
print(Postfix(s1))
s3=''.join(reversed(s3))
print(s3)
print(Prefix(s1))


            
