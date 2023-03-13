# coding:utf-8


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            # 班长从头走到尾
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return


# [1, 2,3 ,4 ,5, 6]



# i 0 ~ n-2   range(0, n-1) j=0
# i 0 ~ n-3   range(0, n-1-1) j=1
# i 0 ~ n-4   range(0, n-1-2) j=2
# j=n  i  range(0, n-1-j)
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

# for j in range(len(alist)-1,0,-1)
#
# [n-1, n-2, n-3, n-4,..., 1]
# for i in range(j)
#
# [0, 1, 2, 3,...,n-2]
# for i in range(n-1-j)