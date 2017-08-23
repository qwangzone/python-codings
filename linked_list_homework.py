class Node():
    def __init__(self, element, the_next=None):
        #即保护类型只能允许其本身与子类进行访问
        #element 元素
        #the_next 下一个节点
        self._el = element
        self.next = the_next
    def __str__(self):
        return "%s,%s" % (self._el, self.next)
    @property
    def element(self):
        return self._el

    def getNext(self):
        return self.next

    def setElement(self, newElement):
        self.element = newElement

    def setNext(self, newNext):
        self.next = newNext
class LinkedList():

    def __init__(self):
        #初始化链表
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def get_head(self):
        return self._head

    def is_empty(self):
        return self._size == 0

    def add_first(self, element):
        newest = Node(element)
        newest.setNext(self._head)
        self._head = newest
        self._size = self._size + 1

    def add_last(self, element):
        newest = Node(element)
        # if self.is_empty():
        #     newest = self._head
        # else:
        #     tmp = self._head
        #     while tmp.getNext()!=None:
        #         tmp = tmp.getNext()
        #     tmp.setNext(newest)
        newest.next = None
        tail = self.find_tail()
        if tail is None:
            self._head = newest
        else:
            tail.next = newest
        self._size = self._size + 1
        print(tail)



    def find_tail(self):
        if self._head is None:
            return None
        else:
            tmp = self._head
            while tmp.next:
                tmp = tmp.next
            return tmp


    def remove_first(self):
        if self._head is None:
            raise Exception("List is empty", "啥东西")
        else:
            tmp = self._head
            self._head = self._head.next
            print(tmp.element)
            return tmp.element

    # zero based
    def get(self, index):
        if index < 0 or index > self._size:
            raise Exception('Index out of range')
        else:
            tmp = self._head
            while index > 0:
                tmp = tmp.next
                index = index - 1
            return tmp.element
if __name__ =='__main__':
    link = LinkedList()
    link.add_first(3)
    link.add_last(5)
    link.add_last(6)
    link.add_last(7)
    link.remove_first()
    print(link.get(1))