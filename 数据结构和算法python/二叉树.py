#is True 和 is not None 区别开
#要确定一棵树，必须要中序+前序后序其中一个

class Node(object):

    def __init__(self,item,lchild=None,rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild
        
class Tree(object):
    def __init__(self):
        self._root = None
    
    def add(self,item):
        node = Node(item)
        if self._root is None:
            self._root = node
            return
        queue = [self._root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
                
    def breadth_travel(self):
        if self._root is None:
            return
        queue = [self._root]
        while(queue):
            cur_node = queue.pop(0)
            print(cur_node.item,end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
                
    def pre_order(self,node):
        if node is None:
            return
        print(node.item,end=' ')
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)
        
        
    def in_order(self,node):
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.item,end=' ')
        self.in_order(node.rchild)
    
    def post_order(self,node):
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.item,end=' ')

if __name__=='__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
 #   tree.breadth_travel()
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print('')
    tree.pre_order(tree._root)
    print('')
    tree.in_order(tree._root)
    print('')
    tree.post_order(tree._root)