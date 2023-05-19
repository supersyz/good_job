###注意！  while条件判断时，要考虑r < n and s[r] != ' ' 哪个在前哪个在后。



class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        n = len(s)
        l,r = 0,0
        #print(s[3])
        while l < n:


            if s[l] != ' ':
                r = l
                while r < n and s[r] != ' ' :
                    r += 1
                ans.append(s[l:r])
                l = r + 1
            else:
                l += 1
        
        ans = ans[::-1]
        return ' '.join(ans)