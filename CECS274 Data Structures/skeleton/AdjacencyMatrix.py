"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import ArrayList
import ArrayStack
import ArrayQueue

class AdjacencyMatrix(Graph):
    def __init__(self, n : int):
        self.n = n
        #This is for boolean matrix
        self.a = self.new_boolean_matrix(self.n)
        #self.a = np.zeros(self.n, object)
    def add_edge(self, i : int, j : int):
        # todo
        self.a[i][j] = True
        
    def remove_edge(self, i : int, j : int):
        # todo
        if self.a[i][j] == False:
            print("Does not Exist")
            return None
        self.a[i][j] = False
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo
        return self.a[i][j]
        
    def out_edges(self, i) -> List:
        # todo
        l = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(i,j):
                l.append(j)
                #print(i,j)
        return l

    def in_edges(self, j) -> List:
        # todo
        l = ArrayList.ArrayList()
        for i in range(self.n):
            if self.has_edge(i,j):
                l.append(i)
                #print(i,j)
        return l

    def bfs(self, r : int):
        # todo
        seen = np.zeros(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i)
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r : int):#dest :int
        # todo
        seen = np.zeros(self.n)
        s = ArrayStack.ArrayStack()
        #r=0#change
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            if i is not None: print(i)
            #elif i == None: print("")
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                else:
                    continue
                    #print("{i} and {j} are in a cycle")
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.a[i].__str__())
        return s
    
    def new_boolean_matrix(self,n):
        return np.zeros([n, n], np.bool_)




