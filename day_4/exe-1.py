'''The following are some of python libraries list: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
 Join the list with a hash with space string.'''
l = ['Django','Flask','Pyramid','Bottle','Falcon']
print('#'.join(l))
'''
    Make the following using string formatting methods:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
x = 8
y = 6
print('{} + {} = {}'.format(x,y,x+y))
print('{} - {} = {}'.format(x,y,x-y))
print('{} * {} = {}'.format(x,y,x*y))
print('{} / {} = {}'.format(x,y,x/y))
print('{} % {} = {}'.format(x,y,x%y))
print('{} // {} = {}'.format(x,y,x//y))
print('{} ** {} = {}'.format(x,y,x**y))