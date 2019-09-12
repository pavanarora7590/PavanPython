class MyDeQue (object):
    def __init__(self):
        self.items = []
    def isDeQueEmpty(self):
        return self.items == []
    def AddDeQueFront(self,item):
        return self.items.insert(0, item)
    def DelDeQueFront(self):
        return self.items.pop(0)
    def AddDeQueBack(self,item):
        return self.items.append(item)
    def DelDeQueBack(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isPresent(self,item):
        if item in self.items:
            return True
        else:
            return False