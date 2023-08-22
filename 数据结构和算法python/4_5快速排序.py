#注意，是先x_mid取出来存在x_mid，然后空出了一个位置来，才开始不停给ls[low],ls[high]赋值
#所以要注意顺序，否则把某个值给覆盖了
#最优时间复杂度 O(nlogn)   每一层复杂度为O(n),要分到只剩一个元素为止，因为每次最优是从正中间拆，所以需要logn次，所以为nlogn
#最坏时间复杂度 O(n**2)    假设每次都最倒霉，就得分n次才行，所以为n**2
#不稳定

def quick_sort(ls,start,end):
    
    #n = len(ls)
    low = start
    high = end 
    x_mid = ls[start]
    if start >= end:
        return
    while(low<high):
        while(low<high):
            if ls[high] > x_mid:
                high -= 1
            else:
                ls[low] = ls[high]
                low += 1
                break
        while(low<high):
            if ls[low] <= x_mid:
                low += 1
            else:
                ls[high] = ls[low]
                high -= 1
                break

    ls[low] = x_mid
    quick_sort(ls,start,low)
    quick_sort(ls,low+1,end)


def quick_sort1(ls,start,end):
    

    low = start
    high = end
    mid_value = ls[start]
    if start >= end:
        return
    while low < high:
        while low < high:
            if ls[high] < mid_value:
                ls[low] = ls[high]
                low +=1
                break
            else:
                high -= 1
                
        
        while low < high:
            if ls[low] > mid_value:
                ls[high] = ls[low]
                high -= 1
                break
            else:
                low += 1
    
    ls[low] = mid_value
    quick_sort(ls,start,low)
    quick_sort(ls,low+1,end)
                
        
    







alist = [54,26,93,17,77,31,44,55,20]
quick_sort1(alist,0,len(alist)-1)
print(alist)