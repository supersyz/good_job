#切片的复杂度为O(1),主要时间复杂度在合并过程中
#每层复杂度都为O(n)，有logn层，所以为nlogn，最优最差都是的
#稳定
#空间上有额外开销，同等的，O(n)

###快排必须掌握，另外再掌握一两种

def merge_sort(ls):
    n = len(ls)
    if n <= 1:
        return ls
    
    mid = n // 2
    left_ls = ls[:mid]
    right_ls = ls[mid:]
    
    left_ls = merge_sort(left_ls)
    right_ls = merge_sort(right_ls)
    
    left_ind,right_ind = 0,0
    merged_ls = []
    while(left_ind<len(left_ls) and right_ind<len(right_ls)):
        if left_ls[left_ind] <= right_ls[right_ind]:
            merged_ls.append(left_ls[left_ind])
            left_ind += 1
        else:
            merged_ls.append(right_ls[right_ind])
            right_ind += 1
    merged_ls = merged_ls + left_ls[left_ind:] + right_ls[right_ind:]
    return merged_ls

alist = [54,26,93,17,77,31,44,55,20]
alist = merge_sort(alist)
print(alist)
        