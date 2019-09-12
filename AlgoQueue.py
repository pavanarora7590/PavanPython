from AlgoStack import MyStack
class MyQueue (object):
    def __init__(self):
        self.items = []
    def isQueueEmpty(self):
        return self.items == []
    def enQueue(self,item):
        return self.items.insert(0, item)
    def deQueue(self):
        return self.items.pop(-1)
    def size(self):
        return len(self.items)
    def isPresent(self,item):
        if item in self.items:
            return True
        else:
            return False
    def callOtherClass(self,item):
        self.item = MyStack()
        #self.item.push(45)
        return self.item.isStackEmpty()