import math
def heapify(arr, n, i):
    largest = i  # 将当前父节点设为最大值
    left = 2 * i + 1  # 左子节点的索引
    right = 2 * i + 2  # 右子节点的索引
    #arr[largest][1]去判断和用arr[i][1]判断是有区别的：用i是分别用父节点跟两个子节点比较，用largest是
    #用左和父中大的那个节点跟右比较
    # 检查左子节点是否比父节点大
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 检查右子节点是否比父节点大
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是父节点，则进行交换
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # 递归地堆化子树
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 构建最大堆（从最后一个非叶节点开始堆化）
    for i in range(n // 2 - 1, -1, -1):
        print(i)
        heapify(arr, n, i)

    # 从堆中提取元素，逐个放入已排序的部分
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换根节点和最后一个节点
        #注意传入i是限制剩余堆进行堆化，传入0是因为这个堆只有根节点变动了，除了根节点外排序好了已经。
        heapify(arr, i, 0)  # 对剩余的堆重新进行堆化

    return arr


# 示例用法
arr = [4,3,3,2,2,2,1,1,1,1]
sorted_arr = heap_sort(arr)
print("排序后的数组：", sorted_arr)