it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#length of it_companies
print(len(it_companies))

it_companies.add('twitter')
print(it_companies)

it_companies.update('a','b','c')
print(it_companies)

it_companies.remove('a')
print(it_companies)

#union of A and B
print(A.union(B))
print(A)

#intersection of A and B
print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))

new_age = set(age)
print(len(age))
print(len(new_age))

if len(age)>len(new_age):
    print('Hello')
else:
    print("World")

new = 'I am a teacher and I love to inspire and teach people'
new_st = list(new.split(' '))
print(new_st)
print(len(new_st))
st = set(new_st)
print(len(st))
print(st)