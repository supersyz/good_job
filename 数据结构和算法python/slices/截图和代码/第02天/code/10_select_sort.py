# alist = [17, 20,         93,54,77,31,44,55,226]
#          0   1         2   3  4  5  6  7  8
#
# j=0
# min = 0  0+1
# alist[0], alist[3] = alist[3], alist[0]
#
# j=1
# min = 1  1+1
# alist[1], alist[8] = alist[8], alist[1]
# j=2
# min = 2  2+1

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1): # j: 0 ~ n-2
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [9 , 16, 17, 15, 11,     (26,1),     (26,2)]

    print(li)
    select_sort(li)
    print(li)