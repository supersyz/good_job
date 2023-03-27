#1.先判断是否有环：有环的话会无限循环，那么可以来个跑的快的指针和跑的慢的指针，如果能相遇就最好
#2.追到的时候公式推理，及细节。见https://www.programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#%E8%A1%A5%E5%85%85
#注意，为什么慢的会走在一圈内的分析！


##判断是否存在，就要想到hash表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. 判断是否有环
        fast,slow = head,head
        flag = 0
        b = head
        while fast is not None and fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = 1
                while True:
                    if fast == b:
                        return fast
                    fast = fast.next
                    b = b.next
                    
        
        if flag == 0:
            return None
        

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. 判断是否有环
        cur = head
        dic = {}
        while cur is not None:
            if cur in dic:
                return cur
            dic[cur] = 1
            cur = cur.next
        return None
