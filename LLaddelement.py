class LLsingle1 ():
    def __init__(self,value):
        self.value = value
        self.nextnode = None
a = LLsingle1(1)
b = LLsingle1(2)
c = LLsingle1(3)
d = LLsingle1(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = None
#print (head.value,middle.value,tail.value,tail.nextnode.value)
#inplace = 50 
#input('enter the node element after which you want to add the new element in linked list ')
#invalue = input('enter the value of the new element ')
#new = LLsingle1(55)
#if inplace == 'head':
#    print ("head it is")
#    newheadV=new.value
#    oldheadV=head.value
#    head.value = newheadV
#    head.nextnode = new



#def cyclecheck (node):
print (a.value,a.nextnode.value,b.nextnode.value, c.nextnode.value)
def reverseLL (node):
    current = node
    previous = None
    nextnode = None
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    return previous
reverseLL(a)
print (d.value,d.nextnode.value,c.nextnode.value,b.nextnode.value)

'''find nth from last, start by i = a then   while a.next != None, assign j as i and intcount=0. now again while j.next != None,ic++ and j=j.next; back in i while loop if ic == n-2 return i.value or else i=i.next'''
  