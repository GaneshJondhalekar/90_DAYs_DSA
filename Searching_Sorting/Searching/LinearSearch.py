
def LinearSearch(l,target):
    for loc in range(len(l)):
        if l[loc]==target:
            return loc
    return 'No target found'

l=[1,3,23,2,56,34]
print(LinearSearch(l,23))
print(LinearSearch(l,20))