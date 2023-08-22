#pop后交换in和outque就可以了
#可以用一个队列实现栈，只需要把队列的输出重新入队列即可

from collections import deque
class MyStack:

    def __init__(self):
        self.inque = deque()
        self.outque = deque()

    def push(self, x: int) -> None:
        self.inque.append(x)

    def pop(self) -> int:
        if len(self.inque) > 1:
            for i in range(len(self.inque)-1):
                self.outque.append(self.inque.popleft())
            pop_item = self.inque.pop()
            while self.outque:
                self.inque.append(self.outque.popleft())
            return pop_item 
        elif len(self.inque) == 1:
            pop_item = self.inque.pop()
            return pop_item 
        else: 
            return None
    def top(self) -> int:
        top_item = self.pop()
        self.push(top_item)
        return top_item

    def empty(self) -> bool:
        return not self.inque


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()





from collections import deque
class MyStack:

    def __init__(self):
        self.inque = deque()
        self.outque = deque()

    def push(self, x: int) -> None:
        self.inque.append(x)

    def pop(self) -> int:
        if len(self.inque) > 1:
            for i in range(len(self.inque)-1):
                self.outque.append(self.inque.popleft())
            pop_item = self.inque.pop()
            self.inque,self.outque = self.outque,self.inque
            # while self.outque:
            #     self.inque.append(self.outque.popleft())
            return pop_item 
        elif len(self.inque) == 1:
            pop_item = self.inque.pop()
            return pop_item 
        else: 
            return None
    def top(self) -> int:
        top_item = self.pop()
        self.push(top_item)
        return top_item

    def empty(self) -> bool:
        return not self.inque


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


from collections import deque
class MyStack:

    def __init__(self):
        self.inque = deque()

    def push(self, x: int) -> None:
        self.inque.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        for i in range(len(self.inque)-1):
            self.inque.append(self.inque.popleft())
        pop_item = self.inque.popleft()
        #self.inque,self.outque = self.outque,self.inque
        # while self.outque:
        #     self.inque.append(self.outque.popleft())
        return pop_item 

    def top(self) -> int:
        top_item = self.pop()
        self.push(top_item)
        return top_item

    def empty(self) -> bool:
        return not self.inque


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()