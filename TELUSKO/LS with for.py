pos = -1
def linearsearch(list,n):
    i=0
    for i in range(n):
        if list[i]==n:
            globals()['pos'] = i
            return True
    return False
list=[5,6,7,3,4,8,9]
n=int(input('enter the search value : '))
if linearsearch(list,n):
    print('found at : ',pos +1)
else:
    print('not found')