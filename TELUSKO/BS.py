pos = -1
def binarysearch(list,n):
    l=0
    u=len(list)-1
    mid=(l+u)//2
    for mid in list:
        if n==mid:
            globals()['pos']=mid
            return True

        elif n<mid:
            u=mid
        else:
            l==mid

list=[2,3,6,7,8,34,67,89]
n=int(input('enter the search value : '))
if binarysearch(list,n):
    print('found ')
else:
    print('not found')