def shell_sort(ls):
    #gaps = [4,2,1]
    n = len(ls)
    gap = n //2 

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

            
alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)