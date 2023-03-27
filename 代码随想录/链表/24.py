#链表问题，先考虑可不可以，需不需要虚拟节点，再考虑先后指向关系。



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        vis = ListNode(next=head)
        cur = vis
        count = 0
        while cur.next.next is not None:
            if count % 2 ==0:
                temp = cur.next.next
                cur.next.next = temp.next
                temp.next = cur.next
                cur.next = temp
                
            cur = cur.next
            count += 1
        return vis.next
        