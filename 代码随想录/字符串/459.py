#重复后掐头去尾，如果还包含原来字符串说明true


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False 

        ls_s = list(s)
        ls_ss = ls_s * 2
        ls_ss.pop(0)
        ls_ss.pop(len(ls_ss)-1)
        ss = ''.join(ls_ss)
        print(ss)
        print(ss.find(s))
        if ss.find(s) == -1:
            return False
        else:
            return True

