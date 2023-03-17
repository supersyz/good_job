#用字典键值对来判断条件




class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = {}
        f,s = 0,0
        ans = 2
        cnt[fruits[s]] = 1
        if len(fruits) <= 2 :
            return len(fruits) 

        while (f<len(fruits)-1):

            while len(cnt) <= 2 and f < len(fruits) - 1:
                f += 1
                if fruits[f] not in cnt:
                    cnt[fruits[f]] = 0
                cnt[fruits[f]] += 1


            ans = max(f - s,ans)


            while len(cnt) > 2:

                cnt[fruits[s]] -= 1
                if cnt[fruits[s]] == 0:
                    cnt.pop(fruits[s])
                s += 1

            ans = max(f - s + 1,ans)
        return ans
                

##优化空间：
#1.内层两个循环，明显是条件对立，所以可以考虑拿一个循环出来，利用外层循环做，又发现第一个内循环部分条件和外循环条件一样。
#2. ans的求值，下面也有上面也有所以可以看一下能不能覆盖。