from AlgoStack import MyStack
from AlgoQueue import MyQueue
from AlgoDeque import MyDeQue
from AlgoQueuewith2stack import MyQueue2Stack
s = MyStack()
print ('MyStack LIFO isEmpty response-> ',s.isStackEmpty())
print ('Load STACK with 1,two,True,4')
s.push(1)
s.push('two')
s.push(True)
s.push(4)
print ('size response--> ', s.size(),'        isEmpty response-->  ',s.isStackEmpty(),'       peek response--> ',s.peek())
print ('two is present--> ',s.isPresent('two'),'      False is present--> ',s.isPresent(False),'      empty is present--> ',s.isPresent(''))
print ('Run a pop')
s.pop()
print ('peek response--> ',s.peek())
print ('Run another pop')
s.pop()
print ('peek response--> ',s.peek())
print ('Run another pop')
s.pop()
print ('isEmpty response-> ',s.isStackEmpty())

t = MyQueue()
print ('\nQueue FIFO isEmptyQueue result',t.isQueueEmpty())
t.enQueue(1)
t.enQueue(2)
t.enQueue(3)
t.enQueue('two')
t.deQueue()
t.deQueue()
print ('t was 1,2,3,two and then dequeue 2 times so its 3,two now')
#t.deQueue()
print ('3 is present->',t.isPresent(3),'       two is present->',t.isPresent('two'),'       1 is present->', t.isPresent(1) )
print ('call stack and check is empty which is always true-->',t.callOtherClass(t))

p = MyDeQue()
print ('\nDeQue isEmptyQueue result',p.isDeQueEmpty())
p.AddDeQueFront(1)
p.AddDeQueFront(2)
p.AddDeQueFront('three')
p.AddDeQueFront(4)
print ('1 is present->',p.isPresent(1),'       2 is present->',p.isPresent(2),'       three is present->', p.isPresent('three'),'       4 is present->', p.isPresent(4) , 'size of deque is ',p.size() )
p.DelDeQueFront()
print ('1 is present->',p.isPresent(1),'       2 is present->',p.isPresent(2),'       three is present->', p.isPresent('three'),'       4 is present->', p.isPresent(4) , 'size of deque is ',p.size() )
p.DelDeQueBack()
print ('1 is present->',p.isPresent(1),'       2 is present->',p.isPresent(2),'       three is present->', p.isPresent('three'),'       4 is present->', p.isPresent(4) , 'size of deque is ',p.size() )
p.AddDeQueBack(4)
print ('1 is present->',p.isPresent(1),'       2 is present->',p.isPresent(2),'       three is present->', p.isPresent('three'),'       4 is present->', p.isPresent(4) , 'size of deque is ',p.size() )
print ('\n Problem 1 Balance Check')
def balance_check(s):
    print ('length of input string is ', len(s))
    if len(s)%2 != 0:
        print ('Fail Unbalanced sequence as string is odd length')
        return 'FAIL'
    openset = { '(','{','['}
    closeset = { ')','}',']'}
    d = { '[':']', '(':')', '{':'}'}
    i=1
    for x in s:
        earlierch = str(s[i-2])
        if x in closeset and earlierch in openset :
#            print ('earlier char is ',earlierch)
            if d[earlierch] != x:
                print ('Fail Unbalanced sequence of brackets as closing of another type found for non match opening')
                return 'FAIL'
                break
        i+=1
#        print (s,i)
    if i == len(s)+1:
        print ('it is balanced sequence')
        return 'PASS'
balance_check('()(){[]}[]')
balance_check('[](){([[[]]])}')
balance_check('()(){]}')
balance_check('(){}[](}[]')

print ('\n Problem 2 Queue with 2 stacks')
prob2 = MyQueue2Stack()
prob2.enQueue(1)
prob2.enQueue(2)
prob2.enQueue(3)
prob2.enQueue(4)
print (prob2.stack1)
print (prob2.stack2)
prob2.deQueue()
print (prob2.stack2)
prob2.deQueue()
print (prob2.stack2)
prob2.deQueue()
print (prob2.stack2)

print (dir(MyStack))