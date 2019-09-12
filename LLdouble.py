cv = (2,3,4)
bc = [2,33]
cd = {1:'erer', 2:45, 3:'ere565', 4:[4,5,6]}
print (cd[4])

class LLdouble1 ():
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.prevnode = None
a = LLdouble1(1)
b = LLdouble1(2)
c = LLdouble1(3)
a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b
print (a.value,b.prevnode.value, a.nextnode.value, c.prevnode.value, b.nextnode.value)
n = LLdouble1(45)






inplace = input('enter the node element after which you want to add the new element in linked list ')
inplace = int(inplace)
invalue = input('enter the value of the new element ')
n = LLdouble1(invalue)

if inplace == a.value:
    print ("true")
    a.nextnode = n
    n.nextnode = b
elif inplace == b.value:
    b.nextnode = n
    n.nextnode = c
elif inplace == c.value:
    c.nextnode = n
    n.nextnode = None
    print ("added element in tail")
else:
    n.nextnode = a
    print ("added element in head")
print (a.value, a.nextnode.value, b.nextnode.value, c.nextnode.value, n.nextnode)



