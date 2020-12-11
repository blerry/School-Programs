import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time
import MaxQueue
import SortableBook
import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = None
        #Queue
        self.shoppingCart = SLLQueue.SLLQueue()
        #indexTitle
        self.indexTitle = ChainedHashTable.ChainedHashTable()
        #Sorted Title
        self.indexSortedTitle = None
        #BinaryHeap
        self.bestSellers = None
        #Sorting
        self.sortedBookCatalog = None
        self.titleCatalog = None
        self.bonusCatalog = None
        #Graphs
        self.indexKeys = None
        

    def loadCatalog(self, fileName : str) :
        #Graphs
        self.indexKeys = ChainedHashTable.ChainedHashTable()
        self.bookCatalog = ArrayList.ArrayList()
        
        with open(fileName) as f:
            start_time = time.time()
            i = 0 #line number
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                sb = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(sb)

                self.indexKeys.add(key, i)
            i++
    def similarGraph(self,size : int): #(self, k)
        with open(fileName) as f:
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1, len(l)):
                    j = indexKeys.find(l[k])
                    print(j)
                    if j is not None:
                        similarGraph.add_edge(i,j)
                i++


        print("Menu")
        AdjacencyList.dfs2()
        AdjanccyList.bfs2()

        #bfs2(r1,r2) is index number of book and r2 is desired distance
        #dfs(r1,r2) both are index of different books
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        '''
        #ChainedHashTable
        self.indexTitle = None
        self.bookCatalog = DLList.DLList()
        self.indexSortedTitle = BinarySearchTree.BinarySearchTree()
        '''
        '''
        #Sort
        self.sortedBookCatalog = ArrayList.ArrayList()
        #Bonus
        self.bonusCatalog = DLList.DLList()
        '''
        '''
        with open(fileName) as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            #setting books.txt to indexTitle instance
            for line in f: 
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
        '''
        '''
            #Loading Catalog for SortableBook
        with open(fileName) as g:
            start_time = time.time()
            for line in g:
                (key, title, group, rank, similar) = line.split("^")
                sb = SortableBook.SortableBook(key, title, group, rank, similar)
                self.sortedBookCatalog.append(sb)
                #Bonus LinkedLists
                self.bonusCatalog.append(sb)
        '''
                '''
        with open("books.txt") as g:
            for line in g:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.indexSortedTitle.add(title,b)
                '''
            #elapsed_time = time.time() - start_time
            #print(f"Loading {self.sortedBookCatalog.size()} books in {elapsed_time} seconds")

'''       
    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        #removeFromCatalog: Remove from the bookCatalog the book with the index i
        #input: 
         #   i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        #addBookByIndex: Inserts into the playlist the song of the list at index i 
        #input: 
            #i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def pathLength(self, i: int, j: int):
        print(self.similaGraph.dfs(i, j))

   
    def searchBookByInfix(self, infix : str) :
        '''
        #searchBookByInfix: Search all the books that contains infix
        #input: 
         #   infix: A string    
        '''
        start_time = time.time()
        for i in range(self.bookCatalog.size()):
                u = self.bookCatalog.get(i)
                if infix in u.title:
                    print("Title: " + u.title +" Key: " + u.key) 
                    #k = self.indexKey.find(u.key)
                    #l = self.similaGraph.out.edges(k)
                    
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        #removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    #new function
    def bestSellingBook(self):
        bestSelling = MaxQueue.MaxQueue()
        cart = self.shoppingCart
        #for i in range(cart.n):
            #bestSelling.add(cart) 
        start_time = time.time()
        while cart.size() > 0:
            bestSelling.add(cart.remove())
        print(bestSelling.max())
        return self

    #new function
    def searchBookByTitle(self, ti : str) :
        start_time = time.time()
        bookTitle = self.indexSortedTitle.find(ti)
        if bookTitle == None:
            print("Empty query")
            
        #checking for duplicate items
        elif self.indexTitle.t[self.indexTitle.hash(ti)].size() > 0:
            chosenItem = input("Duplicate items found, choose which index book to add:")
            self.shoppingCart.add(chosenItem)
            print("Added" + chosenItem + "to shopping cart")
        else:
            self.shoppingCart.add(bookTitle)
            print("Added" + " " + "to shopping cart")
    #HashMap
    def searchByPrefixAdd(self, pfx : str):
        start_time = time.time()
        bookTitle = self.indexSortedTitle.find(pfx)
        if bookTitle == None:
            print("Empty query")
        else:
            self.shoppingCart.add(bookTitle)
            print("Added to shopping cart")

    #Binary Heap Best Sellers
    def searchByPrefix(self, pfx : str, k: int):
        start_time = time.time()
        self.bestSellers = BinaryHeap.BinaryHeap()
        if pfx == None:
            print("Empty query") 
        else:
            for i in range(self.bookCatalog.size()):
                u = self.bookCatalog.get(i)
                if pfx in u.title:
                    self.bestSellers.add(u)
                    print("adding books to bestSellers")
                    u.rank * -1
                    for num in range(k):
                        self.bestSellers.remove()
                        #u.rank *-1
                        print("best sellers: ")
                        print("Title: " + u.title +" Key: " + u.key)

    def binarySearchbyTitle(self, prefix: str):
        self.titleCatalog = ArrayList.ArrayList()
        index = not None
        for i in range(self.sortedBookCatalog.size()):
            book = self.sortedBookCatalog.get(i)
            if prefix in book.title:
                self.titleCatalog.append(str(book.title))
                print(str(book.title))
            
        #sortOption = input('''#Choose sorting option:
                    #      1 Merge Sort titleCatalog 
                     #       2 Quick Sort titleCatalog
                      #      3 Binary Search titleCatalog
                            ''')
        
        if sortOption == "1":
            algorithms.merge_sort(self.titleCatalog)
            print(f"Merge Sort completed")
        elif sortOption == "2":
            algorithms.quick_sort(self.titleCatalog)
            print("Quick Sort completed")
        elif sortOption == "3":
            
            title = input("Enter an Exact Title Prefix: ")
            if title == "": return None
            while index is not None:
               index = algorithms.binary_search(self.titleCatalog, title)
               if index is not None:
                    print("Index: " + str(index))
                    print("Title: " + self.titleCatalog[index])
                    self.titleCatalog.remove(index)
               else:
                    return None
            
    def mergeSortedBooks(self):
        start_time = time.time()
        print("Loading...")
        mergeCatalog = ArrayList.ArrayList()
        with open("books.txt") as g:
                for line in g:
                    (key, title, group, rank, similar) = line.split("^")
                    mergeCatalog.append(title)
        catalog = ArrayList.ArrayList()
        for i in mergeCatalog:
            catalog.append(i)
        algorithms.merge_sort(catalog)
        #for book in catalog:
            #print(book)
        elapsed_time = time.time() - start_time
        print("Sorted")
        print(f"Sort completed in {elapsed_time} seconds")

    def mergeSortedBooksDLList(self):
        start_time = time.time()
        print("Loading...")
        mergeCatalog = DLList.DLList()
        with open("books.txt") as g:
                for line in g:
                    (key, title, group, rank, similar) = line.split("^")
                    mergeCatalog.append(title)
        catalog = DLList.DLList()
        for i in mergeCatalog:
            catalog.append(i)
        algorithms.merge_sort(catalog)
        #for book in catalog:
            #print(book)
        elapsed_time = time.time() - start_time
        print("Sorted")
        print(f"Sort completed in {elapsed_time} seconds")
        
        #BST checking for duplicate items
        elif bookTitle.size() > 0:
            chosenItem = input("Duplicate items found, choose which index book to add:")
            self.shoppingCart.add(chosenItem)
            print("Added" + chosenItem + "to shopping cart")
        else:
            self.shoppingCart.add(bookTitle)
            print("Added" + " " + "to shopping cart")
'''                 
    
