import math

a = int(input())
x = 1
b = 1


while True:

    x = x*b
    b += 1
    
    if x >= a:
        if x == a:
            print('Yes')
        else:
            print('No')    
        break