#字符转转列表，切片，然后反转，再转回字符串

##除了算repear，也可以直接for循环中步长为2k



class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        repeat = n // (2*k)
        for i in range(repeat):
            s[i*2*k:i*2*k+k] = self.rev(s[i*2*k:i*2*k+k])
        if len(s[repeat*2*k:]) >= k:
            s[repeat*2*k:repeat*2*k+k] = self.rev(s[repeat*2*k:repeat*2*k+k])
        else:
            s[repeat*2*k:] = self.rev(s[repeat*2*k:])
        s = ''.join(s)
        return s

    def rev(self,a):
        if len(a) <= 1:
            return a 
        l,r = 0,len(a)-1
        while(l<r):
            a[l],a[r] = a[r],a[l]
            l += 1
            r -= 1
        return a