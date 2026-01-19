

"""""
def area(x):
    return x*x

print(area(5))  """

area = lambda x:x*x

print(area(5))


#use lambda function inside function


def apple(Unit_Price):
    return (lambda num_Of_apples : num_Of_apples*Unit_Price)

x = apple(40)
print('Total amount :',x(12))