class Deque(object):
    def __init__(self):
        self.__queue = []
        
    def is_empty(self):
        return self.__queue == None
    
    def add_front(self,item):
        self.__queue.insert(0,item)
        
        
    def add_rear(self,item):
        self.__queue.append(item)
    
    def remove_front(self):
        return(self.__queue.pop(0))
        
        
    def remove_rear(self):
        return(self.__queue.pop())
        
    def size(self):
        return(len(self.__queue))



if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print (deque.size())
    print (deque.remove_front())
    print (deque.remove_front())
    print (deque.remove_rear())
    print (deque.remove_rear())