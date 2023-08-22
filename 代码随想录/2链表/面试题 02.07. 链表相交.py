
#注意，求长度是否算在复杂度内要注意

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        len_a = 0
        len_b = 0
        while a:
            len_a += 1
            a = a.next
        while b:
            len_b += 1
            b = b.next
        gap = abs(len_a-len_b)
        a = headA
        b = headB
        if len_a > len_b:
            while gap:
                a = a.next
                gap -= 1
        else:
            while gap:
                b = b.next
                gap -= 1
        while a is not None and b is not None:
            if a==b:
                return a
            a = a.next
            b = b.next
        return None

            
