# hash+快排
# 为了把k和v对应上，可以绑定成一个元组再放入列表里
## 可以直接用Counter(nums).most_common(k)得到前k频率的(k,v)列表

#用堆排序,因为是要求最大的几位，所以可以用最大堆，然后return最后几位的reverse也可以最小堆return前k个元素
#或者最大堆，pop k次，时间复杂度nlogn


#用堆排序的nlogk方法：只维护长度为k的堆，这个堆即为前k个频率最大的值。维护时，由于要不停弹出，最后留下来的是最大的，所以
#要用小根堆，即头节点是最小的，然后每插入一个值就排序堆，然后pop出头节点。

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
        

        from collections import Counter
        import math


        cnt = Counter(nums)
        itms = list(cnt.items())
        print(itms)
        tmp = itms[:k]

        n = len(itms)
        # for i in range(k//2-1,-1,-1):
        #     self.heaplify(tmp,k,i)
        #
        for j in range(k,n):
            tmp.append(itms[j])
            for i in range((k+1)//2-1,-1,-1):
                self.heaplify(tmp,k+1,i)
            tmp.pop(0)
            print(tmp)
        return [a[0] for a in tmp[::-1]]




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

    