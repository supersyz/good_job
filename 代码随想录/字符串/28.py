# 先h中找到n的头字母，判断h的n长度是不是等于n


##KMP!


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