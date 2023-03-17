#二分法查找可以定位到target值，但是，要注意到删除本身是涉及覆盖的
#所以遇到删除，或者别的情况下先考虑，假设二分法查找到之后，能不能不增加时间复杂度，以及满足题目空间复杂度的情况下完成后续（比如此题删除就需要覆盖操作）
#如果没办法，就舍弃二分法，即舍弃logn时间复杂度，但是n**2暴力穷举显然不合理
#所以考虑n复杂度，即扫一遍就完成。
#因此很容易想到双指针。



#失败二分法案例：  return的是[None,2,2,None], 但是又要处理None

    def removeElement(self, nums: List[int], val: int) -> int:

        
        def search_remove(nums,val,start,end):
            if start > end:
                return nums
            if start == end :
                mid = (start + end) // 2
                if nums[mid] == val:
                    nums[mid:mid+1] = [None]
                return nums
            mid = (start + end) // 2
            if nums[mid] == val:
                nums[mid:mid+1] = [None]
            else:
                nums = search_remove(nums,val,start,mid-1)
                nums = search_remove(nums,val,mid+1,end)
            return nums
    
        nums = search_remove(nums,val,0,len(nums)-1)
        return nums


#考虑一遍扫完：即扫一遍，过程中遇到了target就处理掉。 具体为遇到了target就右边排队每个值赋值给它左边N格的值。这个N其实是缺口，
#是target被覆盖掉后的缺口，所有前面遇到了几个target，N就等于几，这个N就是右边nums[i]赋值给nums[i-N]中的N
#既然要赋值给左边N位前的值，那代码肯定为nums[i-N] = nums[i],所以可以用双指针。 但是i-N会在判断中变化，相对值容易在边界条件出问题，所以可以两个指针都为绝对值

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        
        n = len(nums)
        i = 0
        j = 0
        while i <= n-1:
            if nums[i] == val:
                i += 1
                if i == n:
                    return j
            else:
                i += 1
                j += 1
                if i == n:
                    return j

            nums[j] = nums[i]
        
        return j
    


#更简洁：  while中先搭好以下框架: if xxx判断完后  fast无论如何都 +=1，然后遇到边界退出，这样保证不会在特殊情况下，例如越界，报错
#然后再去填写判断。
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        
        n = len(nums)
        i = 0
        j = 0
        while i <= n-1:
        #更简洁：  while中先搭好以下框架: if xxx判断完后  fast无论如何都 +=1，然后遇到边界退出，这样保证不会在特殊情况下，例如越界，报错
        #然后再去填写判断。
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

            i += 1
        
        return j