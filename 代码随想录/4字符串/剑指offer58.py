
#要想到在本串上改的方法：
##通过局部或者全局翻转达到效果
###反向思考，先局部翻转一下，然后全局翻转一下看下是啥样的，然后就能找到结果

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        a,b = s[:n],s[n:]
        return ''.join([b,a])


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        k = n
        s[:k] = s[:k][::-1]
        s[k:] = s[k:][::-1]
        s = s[::-1]
        return ''.join(s)