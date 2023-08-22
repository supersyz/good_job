##最坏复杂度O(n**2)
# 改进：最优复杂度为O(n)，因为如果第一次内循环发现不用换顺序就说明有序了，
#代码中要体现
#稳定


# def bubble_sort(ls):
#     for j in range(len(ls),1,-1):
#         count = 0
#         for i in range(j-1):
#             if ls[i] > ls[i+1]:
#                 ls[i],ls[i+1] = ls[i+1],ls[i]
#                 count += 1
#         if count == 0: break
                


def bubble_sort1(ls):
    for j in range(len(ls)-1,1,-1):
        count = 0
        for i in range(j):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                count += 1
        if count ==0:
            break
    return ls


li = [54,26,93,17,77,31,44,55,20]
bubble_sort1(li)
print(li)
            

