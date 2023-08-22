###注意！  while条件判断时，要考虑r < n and s[r] != ' ' 哪个在前哪个在后。

##空间复杂度为O（1）的方案：
## 先去空，然后整个字符串反转，然后单词反转
###注意，去空可以分情况，先把头尾的搞定，再搞中间
####因为字符串是不可变类型，所以反转单词的时候，需要将其转换成列表，然后通过join函数再将其转换成列表，所以空间复杂度不是O(1)
####可以用split获取单词，然后双指针

#####split函数自动就把空格给去掉了只剩下单词

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
    
    

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
       #1.去除多余空格

            
        while( s[0] == ' '):
            s = s[1:]
        while s[len(s)-1] == ' ':
            s = s[:-1]
        l = r = 0
        for l in range(len(s)):
           
            while l < len(s) - 1 and s[l] != ' ':
                l += 1

            r = l
            
            while r < len(s) and  s[r] == ' ':
                r += 1
            if l != r:
                s[l:r] = ' '
            #l += 1
            if l >= len(s) - 1:
                break


            
        #2.  反转字符串

        s.reverse()
        #print(s)
        #3. 反转单词
        l = r = 0
        while(l < len(s)):
            r = l
            while r < len(s) and s[r] != ' ':
                r += 1
            s[l:r] = s[l:r][::-1]
            l = r + 1
        return ''.join(s)
    
    
class Solution:
    def reverseWords(self, s: str) -> str:
        #s = list(s)
       #1.去除多余空格
        n = len(s)
        s = s.strip()
        print(s)
        s = s[::-1]
        ans = s.split()


        return ' '.join([text[::-1] for text in ans])
    


class Solution:
    def reverseWords(self, s: str) -> str:
        #s = list(s)
       #1.去除多余空格
        ans = s.split()
        l,r = 0,len(ans)-1
        while l < r:
            ans[l],ans[r] = ans[r],ans[l]
            l += 1
            r -= 1
        return ' '.join(ans)


   
            

        