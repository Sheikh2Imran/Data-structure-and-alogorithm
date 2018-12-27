'''
Name : Stack implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

class stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        return item

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
if __name__=="__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while not s.is_empty():
        print(s.pop())