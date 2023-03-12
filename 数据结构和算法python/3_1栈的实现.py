class Stack(object):
    
    def __init__(self):
        self.__list = []
    
    def is_empty(self):
        return self.__list == None
        
    def push(self,item):
        self.__list.append(item)
    
    def pop(self):
  
        return(self.__list.pop())
    
    def peek(self):
        
        if self.is_empty():
            return None
        else:
            return(self.__list[-1])
    
    def size(self):
        return(len(self.__list))
    
    
if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print (stack.size())
    print (stack.peek())
    print (stack.pop())
    print (stack.pop())
    print (stack.pop())