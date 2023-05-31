#注意哪个在前哪个在后，还有边界条件



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stk = []
        ans = 0
        for i in range(len(tokens)):
            if tokens[i] == '+':
                ans = int(stk.pop()) + int(stk.pop())
                stk.append(ans)
            elif tokens[i] == '-':
                a = int(stk.pop())
                b = int(stk.pop())
                ans = b - a
                stk.append(ans)
            elif tokens[i] == '*':
                ans = int(stk.pop()) * int(stk.pop())
                stk.append(ans)
            elif tokens[i] == '/':
                a = int(stk.pop())
                b = int(stk.pop())
                ans = int( b / a )
                stk.append(int(ans))
            else:
                stk.append(tokens[i])
        return ans

