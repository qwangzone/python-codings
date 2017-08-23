class Node:
    __slots__ = ('_item', '_next')

    def __init__(self, item):
        self._item = item
        self._next = None

    def __str__(self):
        return "%s,%s" % (self._item, self._next)

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setNext(self, newnext):
        self._next = newnext

    def setItem(self, newitem):
        self._item = newitem

class SingleLinkedList:
    def __init__(self):
        #初始化链表为空表
        self._head = None
        self._size = 0
    def __str__(self):
        return "%s,%s" % (self._head,self._size)

    def isEmpty(self):
        return self._head == None

    #在链表前端添加元素
    def addfirst(self, item):
        newitem = Node(item)

        newitem.setNext(self._head)
        self._head = newitem
        # print(self._head)
        # print(self._head.getNext())
        # print("\n")

    #在链表尾部添加元素
    def addlast(self, item):
        newitem = Node(item)
        #若为空表，将添加的元素设为第一个元素
        if self.isEmpty():
            self._head = newitem
        else:
            tmp = self._head
            print(tmp)
            #遍历链表
            while tmp.getNext()!=None:
                tmp = tmp.getNext()
            #此时tmp为链表的最后一个元素
            return tmp.setNext(newitem)

    #检查链表中元素是否存在
    def search(self, item):
        tmp = self._head
        founditem = False
        while tmp != None and not founditem:
            if tmp.getItem()==item:
                founditem = True
            else:
                tmp = tmp.getNext()
        return founditem

    #按照index索引元素在链表中的位置
    def index(self, item):
        tmp = self._head
        count = 0
        found = False
        while tmp != None and not found:
            count+=1
            if tmp.getItem() == item:
                found = True
            else:
                tmp = tmp.getNext()
        if found:
            return count
        else:
            raise Exception('%s is not in linklist'%item)
    #删除链表中某个元素
    def delete(self, item):
        tmp = self._head
        pre = None
        while tmp != None:
            if tmp.getItem() == item:
                if not pre:
                    self._head = tmp.getNext()
                else:
                    pre.setNext(tmp.getNext())
                break
            else:
                pre = tmp
                tmp = tmp.getNext()


if __name__ == '__main__':
    wq = SingleLinkedList()
    wq.addfirst(1)
    wq.addfirst(2)
    wq.addfirst(9)
    wq.addlast(9)
    #wq.delete(9)
    print(wq.index(1))
    print(wq)




