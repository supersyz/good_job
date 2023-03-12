class Node(object):
    
    def __init__(self,item,next=None):
        self.item = item
        self.next = next


class SingleCycLinkList(object):
    
    def __init__(self):
        self._head = None

    def is_empty(self): #链表是否为空
        return self._head == None
    
    
    
    def length(self): #链表长度
        cur = self._head
        if self.is_empty():
            return 0
        count = 1
        while(cur.next != self._head):
            cur = cur.next
            count += 1

        return count
        
        
        
    def travel(self): #遍历整个链表
        cur = self._head
        if self.is_empty():
            return 
        
        while (cur.next != self._head):
            print(cur.item,end=' ')
            cur = cur.next
        print(cur.item)
        print('')
        
    def add(self,item): #链表头部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
            return
  

        cur = self._head
        while(cur.next != self._head):
            cur = cur.next
        node.next = self._head
        cur.next = node
        
        
    def append(self,item): #链表尾部添加元素
        
        ### 如果为空，那就不存在pre.next
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
            node.next = self._head
            return

        while cur.next != self._head:
            cur = cur.next
        cur.next = node
        node.next = self._head
        


        
        
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
        if self.is_empty():
            return 
        cur = self._head      
        pre = None
        #假设不止一个节点
        if cur.item == item:
            #第一个节点删除
            if self.length == 1:
                self._head = None
                return
            while(cur.next != self._head):
                cur = cur.next
                print(cur.item)
            cur.next = self._head.next
            self._head =  self._head.next
            return
        

        while(cur.next != self._head):
            #中间节点删除
            if cur.item == item:
                pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        
        if cur.item == item:
            if self.length() == 1:
                return
            pre.next = self._head
        
        ##只有一个节点时没有pre
            
            
            
        
        
        
        # cur = self._head
        # pre = None
        
        # if self._head.item == item:
        #     self._head = self._head.next
        # else:
        #     while (cur != None):
        #         if cur.item == item:
        #             pre.next = cur.next
        #             break
        #         else:
        #             pre = cur
        #             cur = cur.next
            

        
    def search(self,item): #查找节点是否存在
        cur = self._head
        #pos = 0
        while cur.next != self._head:
            if cur.item == item:
                return True
                
            else:
                cur = cur.next

        return cur.item == item



if __name__ == "__main__":
    ll = SingleCycLinkList()
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
    print (ll.search(3))
    print (ll.search(7))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()