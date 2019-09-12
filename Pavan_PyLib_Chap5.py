print ('normal for loop')
sq1 = []
for x in range(1,6):
    sq1.append(x)
print (sq1)
print ('list conprehension print 1 to 5 JUST 1 LINE')
sq2 = [ x for x in range(1,6)]
print (sq2)
print ('list conprehension print matrix')
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print ('3 rows so x in range (3) and for row in matrix is al rows so run as row(x)')
a = [[row[i] for row in matrix] for i in range(3)]
print ('transpose of matric via list comprehension in one line', a) 
a=[1,2,3,4,5,6,7,8,9,10]
print (a)
del a[1];'''its deleting index'''
print (a)
del a[0:3];'''its deleting index a to index b'''
print (a)
del a[:];'''clearing whole array'''
print (a)
a=[1,2,3,4,5,6,7,8,9,10]
print (a)
a.clear();'''clearing whole array'''
print (a)
a=[1,2,3,4,5,5,5,5,5,5,6,7,8,9,10,5,5]
print (a)
print (a.index(5, 0, 8))
print (a.count(5) )
a.reverse()
print ('reverser list ', a)
c = [ x for x in reversed(a) ]
#c = reversed( a.sort() )
print (c)
