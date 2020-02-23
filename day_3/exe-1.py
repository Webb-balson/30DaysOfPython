age = 23
height = 5.0
comp = 2+3j

print('Calculating area of a triangle')
base = int(input('Enter the base of triangle'))
height = int(input('Enter the height of triangle'))
area = 0.5*base*height
print('The area of triangel is ',area)

print()
print('Now Calculating perimeter of a triangel')
a = int(input('Enter side a:'))
b = int(input('Enter side b:'))
c = int(input('Enter side c:'))
perimeter = a+b+c
print('The perimeter of the triangle is ',perimeter)

print()
print('Now calculating area and perimeter of rectangle')
length = int(input('Enter the length'))
width = int(input('Enter the width'))
area = length*width
perimeter = 2*length*width
print('The area of rectangle is ',area)
print('The perimeter of rectangle is ',perimeter)

print()
print('Now calculating area and circumference of circle ')
radius = int(input('Enter the radius of circle:'))
pi = 3.14
area = pi*radius**2
circumference = 2*pi*radius
print('The area of circle is ',area)
print('The circumference of circle is ',circumference)

print()
print('Calculate the value of x when y is 0')
x = int(input('Enter the value of x '))
y = x**2+6*x+9
print('The value of y is ',y)

print()
print('Is len of python == jargon',len('python')==len('jargon'))

print()
print('on' in 'python' and 'jargon')

print()
print('jargon' in 'I hope this course is not full of jargon')

x = len('python')
print(x)
y = float(x)
print(y)
z = str(y)
print(z)

print()
print('Lets check if a given number is even or not?')
x = int(input('Enter a number'))
if(x%2==0):
    print('Number is even')
else:
    print('Number is odd')

print()
print(type(10) == 10)

print()
print(int(9.8)==10)

print()
print('Calculating pay of person')
x = int(input('Enter hours:'))
y = int(input('Enter rate per hour:'))
print('Your weekly earning is ',x*y)

print()
for i in range(5):
    print(i,'*',i,'=',i**2,' ',i**3)

