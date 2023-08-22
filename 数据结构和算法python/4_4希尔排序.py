#最坏时间复杂度O(n**2)
#最优时间复杂度：根据步长不同不同 n**1.3
#平均复杂度nlogn 到 n**2之间
#不稳定
#时间复杂度与初始顺序无关，可以对大型数组进行高效排序

# def shell_sort(ls):
#     #gaps = [4,2,1]
#     n = len(ls)
#     gap = n //2 

#     while gap >= 1:
#         for j in range(gap,n):
#             i = j
#             while i > 0:
#                 if ls[i] < ls[i-gap]:
#                     ls[i],ls[i-gap] = ls[i-gap],ls[i]
#                     i -= gap
#                 else:
#                     break
#         gap = gap // 2 
def shell_sort(ls):
    #gaps = [4,2,1]
    n = len(ls)
    gap = n // 2
    while gap >= 1:
        for j in range(gap,n):
            i = j
            while i > 0:
                if ls[i] < ls[i-gap]:
                    ls[i],ls[i-gap] = ls[i-gap],ls[i]
                    i -= gap
                else:
                    break
        gap = gap // 2
        
    return ls

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)