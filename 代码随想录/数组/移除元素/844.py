class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def strin(nums):
            fast = 0
            slow = 0
            n = len(nums)
            while (fast < n):
                if nums[fast] != '#':
                    nums[slow] = nums[fast]
                    slow += 1
                    fast += 1
                else:
                    slow -= 1
                    if slow < 0:
                        slow = 0
                    fast += 1
            return slow,nums
        s = list(s)
        t = list(t)
        slow1,nums1 = strin(s)
        slow2,nums2 = strin(t)
        return nums1[:slow1] == nums2[:slow2]

        # return s == t
