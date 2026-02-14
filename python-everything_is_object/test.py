a = 89
b = 90
print(type(a))

print(id(a))

print(id(b))

print(a is b)

b=a
print(a is b)

print(id(a), id(b))

b = a+1
print(id(a), id(b))

s1="best School"
s2= s1
print(s1 is s2)

print(s1 is s2)


s1 = "Best School"
s2 = "Best School"
print(s1 is s2)

l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)


l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)


l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

a = ()
print(type(a))

a = (1, 2)

print(type(a))

a = (1)

print(type(a))

a = (1, )

print(type(a))

a = (1)
b = (1)
print(a is b)

a = (1, 2)
b = (1, 2)
print(a is b)

a = ()
b = ()
print(a is b)

print(id(a))
