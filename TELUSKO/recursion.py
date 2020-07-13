import sys
sys.setrecursionlimit(2000)
i=0
print(sys.getrecursionlimit())
def a():
    global i
    print('hello',i)
    
    i+=1
    a()
a()