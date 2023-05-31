# hash+快排
# 为了把k和v对应上，可以绑定成一个元组再放入列表里

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        items = list(Counter(nums).items())
        print(items)
        items.sort(key=lambda a:a[1],reverse=True)
        ans = [a[0] for a in items]
        return ans[:k]