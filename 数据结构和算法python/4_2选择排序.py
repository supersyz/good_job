##最优最坏都是O(n**2)
##不稳定



def select_sort(ls):
    
    for j in range(len(ls)-1,0,-1):
        min_index = len(ls) -j -1
        for i in range(min_index+1,len(ls)):
            if ls[min_index] > ls[i]:
                ls[min_index],ls[i] = ls[i],ls[min_index]

alist = [54,226,93,17,77,31,44,55,20]
select_sort(alist)
print(alist)