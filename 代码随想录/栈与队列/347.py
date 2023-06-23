# hash+快排
# 为了把k和v对应上，可以绑定成一个元组再放入列表里
## 可以直接用Counter(nums).most_common(k)得到前k频率的(k,v)列表

#用堆排序,因为是要求最大的几位，所以可以用最大堆，然后return最后几位的reverse也可以最小堆return前k个元素
#或者最大堆，pop k次，时间复杂度nlogn


#用堆排序的nlogk方法：只维护长度为k的堆，这个堆即为前k个频率最大的值。维护时，由于要不停弹出，最后留下来的是最大的，所以
#要用小根堆，即头节点是最小的，然后每插入一个值就排序堆，然后pop出头节点


##注意，其实不是插入一个值，因为：如果从尾部节点插入，
#那么需要对每个父节点再做一次建堆！！，一般来说，堆建立一次就不要再反复建了那第一次的建立就没意义了
#如果从头插入，那么其实想象一下根节点只有一个子节点，就不是完全二叉树了！
#所以考虑到上面两个情况，不是要插入然后pop，而是要先用小根堆排好后，
#判断新的值是不是比根节点的值，就是说当前最大k值中最小那个还小，如果还小那就不维护了
#如果要大一点，那么根节点的最小值就不维护了，把根节点的最小值替换！！成那个大一点的值
#再只针对根节点进行一次堆序就好了。
#最后，得到的tmp堆，其实没有排序，输出的时候要自己排下序，那么用堆排序或者快排都可以

#可以用python的heapq库
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        items = list(Counter(nums).items())
        print(items)
        items.sort(key=lambda a:a[1],reverse=True)
        ans = [a[0] for a in items]
        return ans[:k]
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        #print(Counter(nums).most_common(k))
        # items = list(Counter(nums).items())
        # print(items)
        # items.sort(key=lambda a:a[1],reverse=True)
        ans = [a[0] for a in Counter(nums).most_common(k)]
        return ans

    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        from collections import Counter
        cnt = Counter(nums)
        itms = list(cnt.items())
        n = len(itms)
        for i in range(n//2-1,-1,-1):
            self.heaplify(itms,n,i)
        
        for i in range(n-1,0,-1):
            itms[0],itms[i] = itms[i],itms[0]
            self.heaplify(itms,i,0)
        print(itms)
        return [a[0] for a in itms][-1:-k-1:-1]




    def heaplify(self,arr,n,i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        ##arr[largest][1]去判断和用arr[i][1]判断是有区别的：用i是分别用父节点跟两个子节点比较，用largest是
        ##用左和父中大的那个节点跟右比较
        if left < n and arr[largest][1] < arr[left][1]:
            largest = left
        
        if right < n and arr[largest][1] < arr[right][1]:
            largest = right

        if largest != i:
            arr[largest],arr[i] = arr[i],arr[largest]
            self.heaplify(arr,n,largest)

    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        from collections import Counter,deque
        import math


        cnt = Counter(nums)
        itms = list(cnt.items())
        #print(itms)
        tmp = itms[:k]

        n = len(itms)
        for i in range(k//2-1,-1,-1):
            self.heaplify(tmp,k,i)
        
        for j in range(k,n):
            ##tmp.insert(0,itms[j])  #这样插就破坏了原来的完全二叉树了！！！
            if itms[j][1] < tmp[0][1]:
                pass
            else:
                tmp[0] = itms[j]
                self.heaplify(tmp,k,0)
            #tmp.popleft()
        tmp.sort(key=lambda a:a[1],reverse=True)

        return [a[0] for a in tmp]




    def heaplify(self,arr,n,i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        ##arr[largest][1]去判断和用arr[i][1]判断是有区别的：用i是分别用父节点跟两个子节点比较，用largest是
        ##用左和父中大的那个节点跟右比较
       # print(left < n)
       # print(arr[largest][1] > arr[left][1])
        if left < n and arr[largest][1] > arr[left][1]:
            largest = left
        
        if right < n and arr[largest][1] > arr[right][1]:
            largest = right

        if largest != i:
            arr[largest],arr[i] = arr[i],arr[largest]
            self.heaplify(arr,n,largest)



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        from collections import Counter,deque
        import math
        import heapq
        heal = []
        cnt = Counter(nums)
        i = 0
        for key,value in cnt.items():
            heapq.heappush(heal,(value,key))
            i += 1
            if i > k  :
                heapq.heappop(heal)

        heal.sort(key=lambda a:a[0] ,reverse=True)
        return [a[1] for a in heal]
        
    