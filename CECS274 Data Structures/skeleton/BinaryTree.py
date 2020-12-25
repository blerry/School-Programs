import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        # todo
        if u == None: return -1
        d = 0
        while(u != self.r):
            u = u.parent
            d += 1
        return d

    def size(self) -> int:
        return self._size(self.r)
    
    def _size(self, u : Node) -> int:
        # todo, recursive
        if u == None: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        # todo, iterates
        u = self.r
        prv = None
        n = 0
        while u != None:
            if prv == u.parent:
                n += 1
                if u.left != None:
                    nxt = u.left
                elif u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right != None:
                    nxt = u.right
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return n

    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        # todo
        if u == self.nil:
            return 1 + max(self.height(u.left), self.height(u.right))
    
    def traverse(self, u : Node):
        # todo
        if u == None:
            return
            traverse(u.left)
            traverse(u.right)

    def traverse2(self):
        # todo
        u = self.r
        nxt = None
        prv = None
        while u != None:
            if prv == u.parent:
                if u.left != None:
                    nxt = u.left
                elif u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            prv = u
            u = nxt
                    
    def bf_traverse(self):
       # todo
       q = ArrayQueue.ArrayQueue()
       l = list()
       if self.r is not None:
           q.add(self.r)
           l.append(self.r.v)
       while q.size() > 0:
           u = q.remove()
           if u.left is not None:
               q.add(u.left)
               l.append(u.left.v)
           if u.right is not None:
               q.add(u.right)
               l.append(u.right.v)
       with open("books-bfTraverse.txt", 'a', encoding='utf8') as f: f.write(str(l))
       return l
    
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def in_order(self, u : Node, l : list):
        # todo
        if u.left is not None: self.in_order(u.left, l)
        l.append(u.x)
        with open("books-inorder.txt", 'a', encoding='utf8') as f: f.write(u.x)
        if u.right is not None: self.in_order(u.right, l)
        return l
    def pre_order(self, u : Node, l :list):
        # todo
        l.append(u.x)
        with open("books-preorder.txt", 'a', encoding='utf8') as f: f.write(u.x)
        if u.left is not None: self.pre_order(u.left, l)
        if u.right is not None: self.pre_order(u.right, l)
        return l
    def post_order(self, u : Node, l: list):
        # todo
        if u.left is not None: self.post_order(u.left, l)
        if u.right is not None: self.post_order(u.right, l)
        l.append(u.x)
        with open("books-postorder.txt", 'a', encoding='utf8') as f: f.write(u.x)
        return l
    
    def __str__(self):
        l = []
        self.in_order(self.r, l)
        return ', '.join(map(str, l))
