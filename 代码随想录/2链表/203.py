
##修修补补又三年

##两个指针容易边界条件出问题


##可以设置虚拟节点!!
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        head0 = head 
        pre = None

        if cur is not None:
            while cur.val == val:
                cur = cur.next
                head0 = head0.next
                if cur == None:
                    break
        while cur != None:

            if cur.val == val:
                if pre is not None:
                    pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        if pre == None:
            head0 = None
        return head0
    
#一个指针，还是要考虑删除第一个元素的情况
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is not None:
            while head.val == val:
                head = head.next
                if head is None:
                    break
        
        cur = head
        head0 = head
        if cur is not None:
            while cur.next is not None:
                if cur.next.val == val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next



        return head0