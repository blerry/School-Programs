#Larry Delgado CECS274 Sec07
import time
import Calculator
import BookStore
import DLList
import BinarySearchTree
import ArrayList
import algorithms

def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    expr = "" #
    strexpr = ""
    while option != '0':
        print ("""
        1 Check mathematical expression
        2 Set Variable
        3 Set Expression
        4 Print Expression
        5 Evaluate Expression
        0 Return to main menu
        """)
        option=input() 
        if option=="1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
                
        elif option=="2":
            variable = str(input("Introduce the variable: "))
            value = float(input("Now introduce the value of the variable: "))
            print(f"{variable} = {value}")
            calculator.set_variable(variable, value)
        elif option == "3":
            expr = str(input("Introduce the expression: "))
            
            if calculator.matched_expression(expr) == True:
                print("expression is valid")
            else:
                print("expression is invalid")
        elif option == "4":
            
            for char in expr:
                if char.isalpha():
                    strexpr += str(calculator.dict.find(char))
                else:
                    strexpr += char
            print(strexpr)
        elif option =="5":
            if calculator.dict.size() == 0:
                return 0
            else:
                print(expr + " = " + str(calculator.evaluate(expr)) )
    
                    
        ''' 
        Add the menu options when needed
        '''
def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        1 Load book catalog into sortedBookCatalog
        2 Sort bookCatalog using Merge Sort
        3 Sort bookCatalog using Quick Sort
        4 Search by PreFix using Binary Search
        5 Quick Sort Catalog using LinkedList
        6 Merge Sort Catalog using LinkedList
        
        """)
        '''
        6 Remove a book by index from catalog
        7 Add a book by index to shopping cart
        8 Remove from the shopping cart
        9 Search book by infix
        10 Print Best Selling Book
        11 Reverse order of shopping cart
        12 Search books by title
        13 Search book by prefix
        14 Save to file using BF traversal
        15 in-order
        16 pre-order
        17 post-order
        18 Search Book by Prefix BestSellers
        r setRandomShoppingCart
        s setShoppingCart
        0 Return to main menu
        '''
        option=input() 
        if option=="r":
            bookStore.setRandomShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
        elif option =="2":
            print("loading...")
            start_time = time.time()
            algorithms.merge_sort(bookStore.sortedBookCatalog)
            elapsed_time = time.time() - start_time
            print(f"Sort completed in {elapsed_time} seconds")
        elif option =="3":
            print("loading...")
            start_time = time.time()
            algorithms.quick_sort(bookStore.sortedBookCatalog)
            elapsed_time = time.time() - start_time
            print(f"Sort completed in {elapsed_time} seconds")
        elif option =="4":
            bookStore.binarySearchbyTitle(input("Enter a prefix: "))
        elif option =="5":
            print("loading...")
            algorithms.quick_sort(bookStore.sortedBookCatalog)
            print("Sorted")
        elif option =="6":
            print("loading...")
            bookStore.mergeSortedBooksDLList()
            print("Sorted")

        elif option=="7":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="8":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="9":
            bookStore.removeFromShoppingCart()
        elif option=="10":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option =="11":
            bookStore.bestSellingBook()
        elif option =="12":
            bookStore.reverse()
        elif option =="13":
            t = input("Introduce the query to search: ")
            bookStore.searchBookByTitle(t)
        elif option =="14":
            t = input("Introduce the query to search: ")
            bookStore.searchByPrefix(t)
        elif option =="15":
            print("laoding")
            bookStore.indexSortedTitle.bf_traverse()
            print("Saved to File")
        elif option =="16":
            print("laoding")
            bookStore.indexSortedTitle.in_order(bookStore.indexSortedTitle.r, [])
            print("Saved to File")
        elif option =="17":
            print("laoding")
            bookStore.indexSortedTitle.pre_order(bookStore.indexSortedTitle.r, [])
            print("Saved to File")
        elif option =="18":
            print("laoding")
            bookStore.indexSortedTitle.post_order(bookStore.indexSortedTitle.r, [])
            print("Saved to File")
        elif option =="19":
            bookStore.searchByPrefix(input("Introduce the query to search: "), input("Enter K Size"))
            print("loading...")
        ''' 
        Add the menu options when needed
        '''
def menu_dllist():
    dllist = DLList.DLList()
    option =""
    while option != '0':
        print("""
              1 Add to DLList
              2 Remove from DLList
              3 Test Palindrome
              4 Print DLList
              5 Reverse DLList
              0 Return to main menu
            """)
        option = input()
        if option == "1":
            print("Add an element")
            DLList.append(input())
        elif option == "2":
            print("Select index to remove")
            DLList.remove(input())
        elif option == "3":
            dllist.isPalindrome()
        elif option == "4":
            return print(dllist)
        elif option == "5":
            dllist.reverse()

def menu_bt():
    bt = BinarySearchTree.BinarySearchTree()
    blist = ArrayList.ArrayList()
    option = ""
    while option != '0':
        print("""
             1 Add to Binary Tree
             2 Remove from Binary Tree
             3 Display values using BF traversal
             4 Display values using in-order
             5 Display values using pre-order
             6 Display values using post-order
             7 Print height of tree
             0 Return to main menu
             """)
        option = input()
        if option == "1":
            bt.add(input("Enter the string index: "),input("Enter the value: "))
        elif option == "2":
            bt.remove(input("Enter index to be removed: "))
        elif option == "3":
            print(bt.bf_traverse())
        elif option == "4":
            print( bt.in_order(bt.r, []) )
        elif option == "5":
            print( bt.pre_order(bt.r, []) )
        elif option == "6":
           print( bt.post_order(bt.r, []) )
        elif option == "7":
            print(bt.height())
            
#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        3 DLList Options
        4 Binary Tree
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()
        elif option =="3":
                menu_dllist()
        elif option == "4":
                menu_bt()
if __name__ == "__main__":
  main()
