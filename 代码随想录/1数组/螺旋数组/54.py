class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        x_min,x_max = 0,len(matrix[0])
        y_min,y_max = 0,len(matrix)
        x0,y0 = 0,0
        ans = []

        while x_min<=x_max-1 or y_min<=y_max-1:
            for x0 in range(x_min,x_max):
                ans.append(matrix[y0][x0])
            y_min += 1
            if y_min == y_max:
                break
            for y0 in range(y_min,y_max):
                ans.append(matrix[y0][x0])
            x_max -= 1
            if x_min == x_max:
                break
            for x0 in range(x_max-1,x_min-1,-1):
                ans.append(matrix[y0][x0])
            y_max -= 1
            if y_min == y_max:
                break
            for y0 in range(y_max-1,y_min-1,-1):
                ans.append(matrix[y0][x0])
            x_min += 1
            if x_min == x_max:
                break
        return ans
    
        # x_min,x_max = 0,len(matrix[0])
        # y_min,y_max = 0,len(matrix)

        # ans = []
        # flag_tup = [(1,0),(0,1),(-1,0),(-1,-1)]
        # flag = 0
        # 
        # for i in range(y_max*x_max):
        #     ans.append(matrix[x0][y0])
            

        #     move_flag = flag_tup[flag%4]
        #     dx,dy = move_flag
        #     x0,y0 = x + dx , y + dy
        #     if x0 == x_max or y0 == y_max or 