"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        #self.adj = self.new_boolean_array(self.n)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        # todo
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        for k in range(self.adj[i]):
            if self.adj[i].get(k) == j:
                return True
        return False
        
    def out_edges(self, i) -> List:
        # todo
        
        return self.adj[i]

    def in_edges(self, i) -> List:
        # todo
        out = ArrayList.ArrayList()
        for j in range(self.n):
            if has_edge(j,i):
                out.append(j)
        return out
    
    def bfs(self, r : int):#dest:int
        # todo
        seen = np.zeros(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i)
            ngh = self.out_edges(i)
            #print(ngh)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r : int):#dest :int
        # todo
        seen = np.zeros(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            print(i)
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
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def bfs2(self, r: int, k: int):
        d = 0
        seen = self.new_boolean_array(self.n)
        #seen = np.zeros(self.n, np.bool_)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        l = []
        l.append(r)
        while q.size() > 0 and d < k:
            i = q.remove()
            #print(i)
            ngh = self.out_edges(i)
            #print(ngh)
            for j in range(ngh.size()):
                #print(ngh.size()) is 5 
                x = ngh.get(j)
                #print(j) j = 0
                if seen[x] == False:
                    q.add(x)
                    l.append(x)
                    seen[x] = True
            d = d+1
        return l

    def dfs2(self, r1: int, r2: int):
        stack = ArrayStack.ArrayStack()
        seen = self.new_boolean_array(self.n)
        d = np.zeros(self.n,object)
        d[r1] = 0
        l = []
        stack.push(r1)
        while stack.size() > 0:
            i = stack.pop()
            l.append(i)
            #print(i)
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    stack.push(ngh.get(j))
                    #d[j+1] = i + 1
                    d[j] = d[i] + 1
                else:
                    continue
                if j == r2:
                    return d[j]
        return -1 #r1 and r2 not connected

'''
al = AdjacencyList(5)

al.add_edge(1,2)
al.add_edge(2,3)
al.add_edge(3,4)
al.add_edge(4,1)
al.add_edge(1,3)
al.bfs2(1,0)
'''
