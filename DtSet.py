f = {1,2,3}
print type(f)
f.add(4)
f.add('hello')
print f
f.remove(3)
print f
g = set((2,3))
if 2 in g:
    print 'true'
print g
print f

x=f.union(g)
print x