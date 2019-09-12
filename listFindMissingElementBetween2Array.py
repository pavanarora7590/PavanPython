a=[1,2,3,4,6,7,8,9]
b=[3,2,1,8,7,6]
mis_element=[]
for y in b:
    a.remove(y)
for x in a:
    print ('missing element was: %d' %x)