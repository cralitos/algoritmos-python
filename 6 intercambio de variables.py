# Python program to swap two variables

x = 5
y = 10

print("x =", x)
print("y =", y)


# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#without using temporary variable


x, y = y, x
print('The value of x after swapping without temporary: {}'.format(x))
print('The value of y after swapping without temporary: {}'.format(y))
