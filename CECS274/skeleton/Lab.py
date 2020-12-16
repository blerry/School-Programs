'''
import DLList
import algorithms
dl = DLList.DLList()
dl.add(0,2)
dl.add(1,1)
dl.add(2,0)
algorithms.merge_sort(dl)
print(dl)
'''
#Lab ArrayList
'''
import ArrayList

al = ArrayList.ArrayList()
p = "a"
r = "b"
al.append(p)
al.append(r)
al.remove(p)
print(a1)
'''
#Lab 1 Larry Delgado
'''
from RandomQueue import RandomQueue
queue = RandomQueue()

queue.add('a')
queue.add('b')
queue.add('c')
queue.remove()
print(queue)
'''
#Lab 2 Larry Delgado
'''
import SLLStack
import SLLQueue
import DLList
import MaxQueue

sl = SLLStack.SLLStack()
slQ = SLLQueue.SLLQueue()
dlist = DLList.DLList()

sl.push(1)
sl.pop()
print(sl)

slQ.add(1)
slQ.remove()
print(slQ)

dlist.append('R')
dlist.append('E')
dlist.append('A')
dlist.append('D')
dlist.append('S')

print(dlist)
print(dlist.get(0))
print(dlist.reverse())
print(dlist.isPalindrome())

maxQ = MaxQueue.MaxQueue()
maxQ.add(1)
maxQ.add(2)
maxQ.add(3)
print(maxQ.max())
print(maxQ)
'''
#Lab 3 Larry Delgado
'''
from ChainedHashTable import ChainedHashTable

hasht = ChainedHashTable()

hasht.alloc_table(4)
hasht.add(1,"first")
hasht.add(2,"second")
hasht.add(3,"fourth")
hasht.remove(3)
hasht.add(3,"third")
hasht.add(4,"fourth")
hasht.add(5,"fifth")
print(hasht.size())
print(hasht.find(1))
'''
#Lab 4 Larry Delgado
'''
import BinaryTree
import BinarySearchTree
import ArrayList

alist = ArrayList.ArrayList()
bst = BinarySearchTree.BinarySearchTree()

bst.add("one",1)
bst.add("two",2)
bst.add("three",3)
bst.add("four",4)
bst.add("five",5)
bst.add("six",6)

print(bst.bf_traverse())
'''
'''
#Lab 5 Larry Delgado
import BinaryHeap

heap = BinaryHeap.BinaryHeap()
heap.add(2)
heap.add(1)
heap.add(5)
print(heap.size())
heap.remove()
heap.add(4)
heap.add(1)
heap.add(3)
print(heap.size())
'''
#Lab 6 Larry Delgado
'''
import algorithms
c = [4,1,3,5,2]
p = [4,1,3,5,2]
o = [6,5,3,7,8]
m = [2,1]
q = [1,2,3,4]
'''
'''
print(q)
algorithms.binary_search(q,3)
print(q)
'''
'''
print(o)
for i in range(100):
    o = [6,5,3,7,8]
    algorithms.quick_sort(o)
    print(o)
'''
'''
a0 = [2,3]
a1 = [1,4]
a = [3,2,1,4]
algorithms.merge(a0,a1,a)
print(a)
'''
'''
print(c)
algorithms.quick_sort(c)
print(c)
'''
#Lab 7 Larry Delgado
import AdjacencyMatrix
import AdjacencyList
import ArrayQueue

q = ArrayQueue.ArrayQueue()
q.add(0)
print(q)
al = AdjacencyList.AdjacencyList(5)

al.add_edge(1,2)
al.add_edge(2,3)
al.add_edge(3,4)
al.add_edge(4,1)
al.add_edge(1,3)
print(al.bfs(1))
'''
am = AdjacencyMatrix.AdjacencyMatrix(5)
am.add_edge(1,2)
am.add_edge(2,3)
am.add_edge(3,4)
am.add_edge(4,1)
am.add_edge(1,3)
print(am.has_edge(1,2))
print(am.has_edge(1,2))
print(am.in_edges(3))
print(am.out_edges(1))
print(am.dfs(1))
'''


#when finding empty string, shortest book added we make it so it doesnt add anything
#set paremeter to a to when opening file
#add in traversals code on visit u, thats where you write to a file
#put books in binary heap use k as 20 or 10, youll have to remove those from heap
#use search by infix
