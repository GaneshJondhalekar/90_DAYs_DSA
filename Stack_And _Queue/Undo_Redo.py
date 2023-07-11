'''Given an array of strings Q[], consisting of queries of the following types:

“WRITE X”: Write a character X into the document.
“UNDO”: Erases the last change made to the document.
“REDO”: Restores the most recent UNDO operation performed on the document.
“READ”: Reads and prints the contents of the documents.

Input: Q = {“WRITE A”, “WRITE B”, “WRITE C”, “UNDO”, “READ”, “REDO”, “READ”}
Output: AB ABC

Input: Q = {“WRITE x”, “WRITE y”, “UNDO”, “WRITE z”, “READ”, “REDO”, “READ”}
Output:xz xzy    '''

from collections import deque
def Undo_Redo(Q):
    stack1=deque()
    stack2=deque()
    for query in Q:
        if 'WRITE' in query:
            i,j=query.split(' ')
            stack1.append(j)
            continue
        if query=='UNDO':
            stack2.append(stack1.pop())
            continue
        if query=='REDO':
            stack1.append(stack2.pop())
            continue
        if query=='READ':
            print(*stack1,sep='',end=' ')
Q =['WRITE A', 'WRITE B', 'WRITE C', 'UNDO', 'READ', 'REDO', 'READ']
Q1 =['WRITE A', 'WRITE B','UNDO', 'WRITE C','READ', 'REDO', 'READ']
Undo_Redo(Q1)

        