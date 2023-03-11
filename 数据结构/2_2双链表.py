

class Node(object):
    
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

class SingleLinkList(object):
    
    def __init__(self):
        self._head = None

    def is_empty(self): #链表是否为空
        return self._head == None
    
    
    
    def length(self): #链表长度
        cur = self._head
        count = 0
        while(cur != None):
            cur = cur.next
            count += 1

        return count
        
        
        
    def travel(self): #遍历整个链表
        cur = self._head
        while (cur!= None):
            print(cur.item,end=' ')
            cur = cur.next
        print('')
        
    def add(self,item): #链表头部添加元素
        node = Node(item)
        
        node.next = self._head
        self._head = node
        
        
    def append(self,item): #链表尾部添加元素
        
        ### 如果为空，那就不存在pre.next
        node = Node(item)
        pre = self._head
        if self.is_empty():
            self._head = node
        else:
            while(True):
                if pre.next == None:
                    pre.next = node
                    break
                else: 
                    pre = pre.next
        
        
    def insert(self,pos, item): #指定位置添加元素
        node = Node(item)
        cur = self._head
        count = 0
        
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):                 
            self.append(item)
        else:
            while (count < pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
        
        
    def remove(self,item): #删除节点
        
        cur = self._head
        pre = None
        
        if self._head.item == item:
            self._head = self._head.next
        else:
            while (cur != None):
                if cur.item == item:
                    pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next
            

        
    def search(self,item): #查找节点是否存在
        cur = self._head
        #pos = 0
        while cur != None:
            if cur.item == item:
                return True
                
            else:
                cur = cur.next

        return False
                
                
                

class DoubleNode(object):
    def __init__(self,item):
        self.pre = None
        self.next = None
        self.item = item



class DoubleLinkList(SingleLinkList):
    
    def add(self,item):
        #cur = self._head
        empty_flag = self.is_empty()
        node = DoubleNode(item)
        node.next = self._head
        self._head = node
        if not empty_flag:
            node.next.pre = node
        
    
    def append(self,item):
        cur = self._head
        node = DoubleNode(item)
        if self.is_empty():
            self.add(item)
        else:
            while(cur.next != None):
                cur = cur.next
            cur.next = node
            node.pre = cur
            node.next = None
        
    
    def insert(self,pos,item):
        cur = self._head
        node = DoubleNode(item)
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while(count < pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            node.next.pre = node
            cur.next = node
            node.pre = cur
    
    def remove(self,item):
        cur = self._head

        while (cur != None):
            if cur.item == item:
                if cur.pre==None:
                    self._head = cur.next
                    cur.next.pre = None
                else:
                    #print(cur.pre)
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next
        
        
if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    ll.add(1)
    ll.travel()
    ll.add(2)
    ll.travel()
    ll.append(3)
    ll.travel()
    ll.insert(2, 4)
    ll.travel()
    ll.insert(4, 5)
    ll.travel()
    ll.insert(0, 6)
    ll.travel()
    print ("length:",ll.length())
#     ll.travel()
    print (ll.search(3))
    print (ll.search(100))
    ll.remove(5)
    print( "length:",ll.length())
    ll.travel()