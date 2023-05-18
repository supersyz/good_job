#思路同349但是不用set


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        ans = []
        cnt_1 = Counter(nums1)
        cnt_2 = Counter(nums2)
        cnt_key_1 = Counter(cnt_1.keys())
        cnt_key_2 = Counter(cnt_2.keys())
        for k,v in cnt_key_1.items():
            if cnt_key_2[k] == v:
                rp = min(cnt_1[k],cnt_2[k])
                for i in range(rp):
                    ans.append(k)

        return ans