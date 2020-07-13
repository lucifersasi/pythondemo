import sys
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())
i=1
f = int(input('enter the number to get factorial: \n'))
def fact():
    global f
    global i
    f=f*i
    i+=1
    fact()
    return(f)
   # if f==i
   #     break
result=fact()
print(result)