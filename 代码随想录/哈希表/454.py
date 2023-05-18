# 四个数求和为0，可以拆成2个数组和的可能*2个数组和的可能。


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        n = len(nums1)
        sum_A = [i+j for i in nums1 for j in nums2]
        sum_B = [i+j for i in nums3 for j in nums4]
        dic_A = Counter(sum_A)
        dic_B = Counter(sum_B)
        ans = 0
        for k in dic_A:
            if -k in dic_B:
                ans += dic_A[k] * dic_B[-k]

        return ans