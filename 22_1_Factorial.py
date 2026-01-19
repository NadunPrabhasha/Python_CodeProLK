# 4! = 4*3*2*1

x = int(input('Enter Number :'))

result = 1

for i in range(1,x+1):
    result = result*i

print('Result of factorial is :',result)