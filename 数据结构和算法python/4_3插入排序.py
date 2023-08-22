##最优复杂度为O(n),因为左边是排好序的，所以只要第一次判断最右边的数大于左边的最右边的数，就可以break出循环
#最坏复杂度为O(n**2)
#稳定
#两种方式实现，但用while来做判断，就不需要控制len，更灵活，从而希尔排序更好实现。

def insert_sort2(ls):
    n = len(ls)
    for j in range(1,n):
        i = j
        while i > 0:
            if ls[i] < ls[i-1]:
                ls[i],ls[i-1] = ls[i-1],ls[i]
                i -= 1
            else:
                break





# def insert_sort(ls):
#     for left_numbers in range(1,len(ls)):

#         for i in range(left_numbers,0,-1):
#             if ls[i] < ls[i-1]:
#                 ls[i],ls[i-1] = ls[i-1],ls[i]
#             else:
#                 break
                

# def insert_sort(ls):
#     for left_number in range(1,len(ls)):
#         for i in range(left_number,0,-1):
#             if ls[i] < ls[i-1]:
#                 ls[i],ls[i-1] = ls[i-1],ls[i]
#             else:
#                 break
#     return ls
                

alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)
