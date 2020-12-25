from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.n = 0
        self.dummy = DLList.Node("")
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
   
    def get_node(self, i : int) -> Node:
        # todo
        if i < 0 or i > self.n:
            raise IndexError("i out of bounds")
            return None
        if i < self.n//2:
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:
            p = self.dummy #self.dummy.prev
            for k in range(self.n-i):
                p = p.prev
        return p
        
    def get(self, i) -> np.object:
        # todo
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        # todo
        if i < 0 or i > self.n: raise IndexError("i out of bounds")
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y 

    def add_before(self, w : Node, x : np.object) -> Node:
        # todo
        if w == None: raise IndexError("empty")
        #w = self.dummy
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
            
    def add(self, i : int, x : np.object)  :
        # todo
        if i < 0 or i > self.n: raise IndexError("i out of bounds")
        self.add_before(self.get_node(i),x)

    def _remove(self, w : Node) :
       # todo
       w.prev.next = w.next
       w.next.prev = w.prev
       self.n -= 1
       return self
    
    def remove(self, i :int) :
        if i < 0 or i > self.n: raise IndexError("i out of bounds")
        self._remove(self.get_node(i))


    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)
    

    def isPalindrome(self) -> bool :
        # todo
        forward = self.dummy.next
        backward = self.dummy.prev
        
        if forward == None:
            return True
        #forward = backward
        #while backward != backward.next
            #backward = backward.next
        
        while forward != backward:

            if forward.x != backward.x:
                return False
            
            forward = forward.next
            backward = backward.prev

        return True

    def reverse(self):
        # todo
        current = self.dummy.prev
        while current != self.dummy:
            print(current.x) #prints elements in reverse
            current = current.prev
        return self
        
    
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
