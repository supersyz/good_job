class MyLinkedList:

    def __init__(self):
        self._head = None

    def get(self, index: int) -> int:
        cur = self._head
        count = 0
        if index < 0:
            return -1
        while cur != None:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val=val)
        node.next = self._head
        self._head = node

    def addAtTail(self, val: int) -> None:
        cur = self._head
        node = Node(val=val)
        if cur is None:
            self.addAtHead(val)
            return
        while cur.next != None:
            cur = cur.next
        if cur is not None:
            cur.next = node
        else:
            self._head = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val=val)
        cur = self._head
        pre = None
        count = 0
        if index == 0:
            self.addAtHead(val)
            return
        while cur is not None:
            if count == index:
   
                node.next = cur
                pre.next = node
            pre = cur
            cur = cur.next
            count += 1
        if count == index:
            pre.next = node

    def deleteAtIndex(self, index: int) -> None:
        #node = Node(val=val)
        cur = self._head
        pre = None
        count = 0
        if index < 0:
            #self.addAtHead(node)
            return
        if index == 0:
            self._head = self._head.next
            return
        while cur is not None:

            if count == index:
                if cur is not None:
                    pre.next = cur.next
            pre = cur
            cur = cur.next
            count += 1



class Node(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)