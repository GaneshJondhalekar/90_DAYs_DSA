alpha=[chr(i) for i in range(65,91)]
k=29
k=k%26
print(alpha)


def left():
    al=alpha[k:]+alpha[0:k]
    print('left: ',al)
left()

def right():
    al=alpha[26-k:]+alpha[0:26-k]
   
    d={alpha[i]:al[i] for i in range(26)}
    print(d)
right()