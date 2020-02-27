"""Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

"""
front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']
back_end.extend(front_end)
print(back_end)
"""After joining the lists in question 26. Copy the joined list and assigned it to a variable full_stack.
 Then insert, Python and SQL after Redux."""
full_stack = back_end
full_stack.insert(len(full_stack), 'Python')
full_stack.insert((len(full_stack)),'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min = ages[0]
max = ages[-1]
print(min)
print(max)