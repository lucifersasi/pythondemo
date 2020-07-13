lower = int(input('enter lower number: '))
upper = int(input('enter uppernumber: '))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num % i ==0:
                print(num,end="")
                print(' is not prime')
                break
        else:
            print(num, end="")
            print(' is prime')
    else:
        print('num is neither prime nor composite')