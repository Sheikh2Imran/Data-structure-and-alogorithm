'''
Name : Queue implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

class queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    

if __name__=="__main__":
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    while not q.is_empty():
        print(q.dequeue())