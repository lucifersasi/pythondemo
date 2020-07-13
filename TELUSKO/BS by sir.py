pos = -1
def binarysearch(list,n):
   l=0
   u=len(list)-1

   while l<=u:
       mid = (l+u)//2

       if list[mid]==n:
           globals()['pos']=mid
           return pos
       else:
           if list[mid]<n:
               l=mid+1
           else:
               u=mid-1
   return False





list=[3,5,9,12,59,68,79,82,91,108,256]
n=int(input('enter the search value : '))
if binarysearch(list,n):
    print('found at : ',pos +1)
else:
    print('not found')