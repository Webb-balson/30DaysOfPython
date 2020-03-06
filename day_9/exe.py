#1
age = int(input(print('Enter your age! ')))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You are left with ',(18-age) ,' years to drive.')

#2
print('-----------------')
person = {
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'age':250,
'country':'Finland',
'is_marred':True,
'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address':{
    'street':'Space street',
    'zipcode':'02210'
}
}

if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])

if 'skills' in person:
    if 'Node','Python' in person['skills']:
        print(person['skills'])