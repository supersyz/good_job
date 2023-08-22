#思考如何只扫描一遍：
#思考：之前数组学到的知识：想减少扫描次数：增加指针数量，快慢指针！



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        count = 0
        vis = ListNode(next=head)
        slow = vis
  
        while fast is not None:
            while count != n :
                fast = fast.next
                count += 1
            if fast is None:
                break
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return vis.next
