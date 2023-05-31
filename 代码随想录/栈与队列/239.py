#单调队列！


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if len(nums) == 1:
            return [nums[0]]
        dq = deque()
        ans = []
        for i in range(k):
            self._push(nums[i],dq)

        ans.append(self._getmax(dq))
        for i in range(k,len(nums)):
            self._pop(dq,nums[i-k])
            self._push(nums[i],dq)
            ans.append(self._getmax(dq))

        return ans
    
    def _pop(self,dq,value):
        if dq and (dq[0] == value):
            dq.popleft()
        
    def _push(self,value,dq):
        while  dq and (dq[-1] < value):
            dq.pop()
        dq.append(value)

    def _getmax(self,dq):
        return dq[0]


