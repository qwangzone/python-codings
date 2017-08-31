class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size()]

    def show(self):
        print(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.clear()
s.show()