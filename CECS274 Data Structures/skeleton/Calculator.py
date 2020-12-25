import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
            
            
    def matched_expression(self, s : str) -> bool :
        # todo
        stack = ArrayStack.ArrayStack()
        if (len(s) > 0 and s[0] == ')') or s == "":
            return False
        s = '(' + s + ')'
        for character in s:
            if character == '(':
                stack.push(character)
            elif character == ')' and stack.size() != 0:
                stack.pop()
            elif stack.size() == 0:
                return False
        if stack.size() == 0:
            return True
 
    def build_parse_tree(self, exp : str) ->str:
        # todo
        if not self.matched_expression(exp):
            return None
        t = BinaryTree.BinaryTree()
        t.r = t.Node('')
        u = t.r
        operators = ['+','-','*','/','(',')']
        for token in exp:
            if token == '(':
                u = u.insert_left()
            if token in '+-*/':
                u.x = token
                u = u.insert_right()
            if token.isalpha():
               u.x = token
               u = u.parent
            if token == ')':
                u = u.parent
        return t

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        left = root.left
        right = root.right 
        if left != None and right != None:
            fn = op[root.x]
            return fn(self._evaluate(left), self._evaluate(right))
        elif left is None and right is None:
            t = self.dict.find(root.x)
            if t != None: return t
            return root.x
        else:
            if left is not None:
                return self._evaluate(left)
            else:
                return self._evaluate(right)
            
    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        print(parseTree)
        return self._evaluate(parseTree.r)
        
        
