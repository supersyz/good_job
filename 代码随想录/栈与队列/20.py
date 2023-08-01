#这种情况要考虑用栈，一进对应一出

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stk = []
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(')')
            elif s[i] == '{':
                stk.append('}')
            elif s[i] == '[':
                stk.append(']')
            else:
                if not stk:
                    return False
                else:
                    if stk.pop() != s[i]:
                        return False
        if stk:
            return False
        return True
                