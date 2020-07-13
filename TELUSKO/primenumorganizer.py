from array import *
lower = int(input('enter lower number: '))
upper = int(input('enter uppernumber: '))
prime = array('i',[])
composite = array('i',[])


for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num % i ==0:
                prime.append(num)
                break
        else:
            composite.append(num)
    else:
        print('num is neither prime nor composite')
print(prime)
print(composite)