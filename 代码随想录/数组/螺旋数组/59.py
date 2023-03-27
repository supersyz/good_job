# 当列表在二维 [ [ ] ] 或以上时，

# 必须使用 copy.deepcopy() 来进行列表的复制

# 否则原列表和复制列表的子列表会指向同一目标

# 即 id(originalList[0]) == id(copyList[0])

#即：使用  [ [ None ] *n ] *n 方法创建时，会使子列表都指向同一列表
#应当用t = [[None]*n for i in range(n)]

#转起来！
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        w_min,w_max = 0,n - 1
        h_min,h_max = 0,n - 1
        w,h = 0,0
        #ans = [[None]*n]*n 
        ans = [[0] * n for _ in range(n)]
        i = 1
        while i <= n*n:
            for w in range(w_min,w_max+1):
                ans[h][w] = i
                i += 1
            h_min += 1

            for h in range(h_min,h_max+1): 
                ans[h][w] = i 
                i += 1
            w_max -=1

            for w in range(w_max,w_min-1,-1):
                ans[h][w] = i 
                i += 1
            h_max -= 1

            for h in range(h_max,h_min-1,-1): 
                ans[h][w] = i 
                i += 1
            w_min += 1

        return ans
    
    
#