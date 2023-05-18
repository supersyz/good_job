class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        dic_a = Counter(ransomNote)
        dic_b = Counter(magazine)
        for k, v in dic_a.items():
            if k in dic_b:
                v -= dic_b[k]

            if v > 0:
                return False
        return True
    
    
##counter方法
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        #x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        #所以x只保留下了，magazine不能表达的
        if(len(x)==0):
            return True
        else:
            return False