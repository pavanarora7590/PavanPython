a = 5
print (type(a))

a = 12
print (a)


print ('string immutable so can only replace them but cant change a part of string, can refer to elements of tuple via index')
b = 'hello'
print (b[1])
print (type(b))
b = b.replace('e', 'f')
print (b)
print ('tuple immutable so can only replace them but cant change a part of string')
print ('tuple can create another tuple which is sub part of one, or can refer to elements of tuple via index')
c = (1,2,'fg')
print (type(c))
print (c[0], c)
c = c[0:2]
print (c,type(c))
print('test commit via pycharm 123')
