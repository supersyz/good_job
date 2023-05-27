# 先h中找到n的头字母，判断h的n长度是不是等于n


##KMP!
###优雅一点
####可以发现求net的过程和匹配的过程非常相似，可以说，求net[i]的值，就是将i跟net前面的部分进行匹配

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1
        
        h,n = 0,0
        while h < len(haystack):
            if haystack[h] == needle[0]:
                if haystack[h:h+len(needle)] == needle:
                    return h

            h += 1
        return -1
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1 
        net = self.get_next(needle)
        #print(net)
        # h,n = 0,0
        # while(h < len(haystack)):
        #     print(haystack[h])
        #     if haystack[h] == needle[n]:
        #         h += 1
        #         n += 1
        #     else:
        #         if n > 0:
        #             n = net[n-1]

        #     if n == 0:
        #         if not haystack[h] == needle[n]:
        #             h += 1
        #     if n == len(needle):
        #         return h - len(needle)
        n = 0
        for h in range(len(haystack)):
            while n > 0 and haystack[h] != needle[n]:
                n = net[n-1]
            if haystack[h] == needle[n]:
                n += 1
            if n == len(needle):
                return h - len(needle) + 1
        return -1
                



    def get_next(self,needle):
        net = [0]
        j = 0
        for i in range(1,len(needle)):
            while(j > 0 and needle[i] != needle[j]):
                j = net[j-1]
            if needle[i] == needle[j]:
                j += 1
            net.append(j)
        return net