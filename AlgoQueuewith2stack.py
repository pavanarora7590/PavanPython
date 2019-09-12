#from AlgoStack import MyStack
class MyQueue2Stack (object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enQueue(self,item):
        return self.stack1.append(item)
    def deQueue(self):
        #if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()