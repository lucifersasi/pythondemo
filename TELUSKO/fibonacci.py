n=int(input('enter the number of fibonacci series: \n'))
def fib(n):
    a=0
    b=1
    if n < 0:
        print('invalid try another number')
    elif n==1:
        print('fibonacci series:\n',a)
    else:
        print(a,'\n',b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c

            print(c)

fib(n)


