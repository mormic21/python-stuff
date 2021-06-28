v = [0,1,2,3]
print(v[0])
print(v[-1])
print(v[-2])
a = v + [4,5,6]
print(a)
v[0] = -1
print(v)
v[0] = v[1]*v[2]
print(v)
v =v +[4,5,6]
print(v)
v.append(12)
print(v)
y = [a,v]
print(y)

#listen als strings

q = 3*'hi'
print(q)
q = 3*'hi' + 4*'ho'
print(q)
one = 'hi'
two = 'ho'
print(one+two)
print(one[0])
one = "das ist ein text"
print(one[5-8])
print(one[-1])
#von bis - teilstring
print(one[4:8])
#ohne angabe autom. 0
print(one[:3])
print(one[-4:])
one = 'du' + one[4:]
print(one)
print(len(one))
