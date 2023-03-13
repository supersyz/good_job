#递归如果index都是在原本ls上的话，就不要赋值给新ls，否则index会乱，新的ls的index和原本的是不一样的
#时间复杂度： 最坏时间复杂度O(logn)： 最优O(1)




def binary_search(ls,item,start,end):
    
    if start == end or start == end-1:
        if ls[start] == item:
            return start
        elif ls[end] == item:
            return end
        else:
            return False
    mid = (start + end) // 2
    if ls[mid] == item:
        index =  start + mid
    
    elif item < ls[mid]:
        #left_ls,right_ls = ls[:mid],ls[mid:]
        index = binary_search(ls,item,start,mid)

    elif item > ls[mid]:
       # left_ls,right_ls = ls[:mid],ls[mid:]
        index = binary_search(ls,item,mid+1,end)
    return index
    
    
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 100,0,len(testlist)-1))
print(binary_search(testlist, 13,0,len(testlist)-1))
#binary_search(0,len(ls)-1)