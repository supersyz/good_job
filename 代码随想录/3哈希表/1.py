#用字典先判断flag，若true再找，注意不能找自己

##考虑字典，key是值，value是索引。 但是字典会导致相同值出现相同key就被覆盖了，所以不要初始化整个序列为字典，而是设置一个current_dict，每pass一个，存进字典。


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import Counter
        from copy import deepcopy
        cnt = Counter(nums)
        cnt_bk = deepcopy(cnt)
        flags = False
        for i in range(len(nums)):
            cnt[nums[i]] -= 1
            if cnt[nums[i]] == 0:
                cnt.pop(nums[i])
            if target - nums[i] in cnt:
                flags = True
            if flags:
                for j in range(len(nums)):
                    if j == i:
                        continue
                    else:
                        if nums[j] == target - nums[i]:
                            return [i,j]

        


        return False
    
    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current_dict = dict()
        for index,value in enumerate(nums):
            if target - value in current_dict:
                return [current_dict[target-value],index]
            else:
                current_dict[value] = index
        


        return False