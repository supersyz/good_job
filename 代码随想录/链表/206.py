#要一个pos储存
#2.递归，想到递归是因为从后往前，每一步操作都是一样的
#先考虑最后一步递归的操作
#3. LIFO 典型的栈
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fakeh = ListNode(val=None,next=None)
        #fake_l = ListNode(val=0,next=None)
        cur = head
        pre = fakeh
        if head is None:
            return head
        pos = cur.next
        while cur.next != None:
            #if pre.val is not None:
            if pre.val is None:
                cur.next = None
            else:
                cur.next = pre
            pre = cur
            cur = pos
            pos = pos.next
        if pre.val is not None:
            cur.next = pre
            
            

        return cur
    
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 递归终止条件
        
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    
    


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 递归终止条件
        
        stack = []
        cur = head
        while(cur!=None):
            stack.append(cur)
            cur = cur.next
        
        vis_h = ListNode()
        cur0 = vis_h
        while stack:
            cur0.next = stack.pop()
            cur0 = cur0.next
        cur0.next = None
        return vis_h.next
