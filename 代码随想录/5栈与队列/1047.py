#这种abba的形式就要想到用栈


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if stk and s[i] == stk[-1]:
                stk.pop()
            else:
                stk.append(s[i])
        return ''.join(stk)