#笨办法：单指针，遍历，时间复杂度为
##  用双指针
### 判断时候，list_a == list_b会快很多



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        ans = []
        #sorted_p = sorted(p)
        if len(s) < len(p):
            return []
        count_p = Counter(p)
        for i in range(len(s)-len(p)+1):
            count_com = Counter(s[i:i+len(p)])
            mi = count_com-count_p
            if len(mi) == 0:

            #if sorted(s[i:i+len(p)]) == sorted_p:
                ans.append(i)
        return ans
        # for i in range(len(s)-len(p)+1):


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        ans = []
        #sorted_p = sorted(p)
        if len(s) < len(p):
            return []
        count_p = Counter(p)
        count_com = Counter(s[0:len(p)])
        mi = count_com-count_p
        if len(mi) == 0:

        #if sorted(s[i:i+len(p)]) == sorted_p:
            ans.append(0)


        for i in range(1,len(s)-len(p)+1):
            
            count_com[s[i-1]] -= 1
            if count_com[s[i-1]]  == 0:
                count_com.pop(s[i-1])

            # print(i)
            #print(i+len(p))
           # print(i + len(p))

                
            
            count_com[s[i+len(p)-1]] += 1

            mi = count_com-count_p
            if len(mi) == 0:

            #if sorted(s[i:i+len(p)]) == sorted_p:
                ans.append(i)
            
        return ans
        # for i in range(len(s)-len(p)+1):


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        if len(s) < len(p):
            return []
        ans = []
        count_p = [0] * 26
        count_s = [0] * 26
        for i in p:
            count_p[ord(i) - ord('a')] += 1

        
        for j in range(len(p)):
            count_s[ord(s[j])-ord('a')] += 1
        
        if count_p == count_s:
            ans.append(0)

        for i in range(1,len(s)-len(p)+1):
            count_s[ord(s[i-1])-ord('a')] -= 1
            count_s[ord(s[i-1+len(p)])-ord('a')] += 1
            if count_p == count_s:
                ans.append(i)

        return ans

