# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:19:25 2019

@author: Mikef
"""

from RBTree import RedBlack
#Code courtiously provided by a classmate, Kimberly Arenas, for a fuctioning Red Black Tree
#because mine didn't work. I hope that's alright.

from BTrees import BTree
#Code taken from Blackboard, provided by Diego Aguirre. Programmed originally by Olac Fuentes
#edited by Diego Aguirre.

import time

class Node(object):
    def __init__(self, data = None, height = 0):
        self.key = data
        self.height = height
        self.left = None
        self.right = None
        self.parent = None

class AVLBBST(object):
    def __init__(self, root = None):
        if (root != None):
            self.root = Node(root)
        else:
            self.root = root
    
    def AVLTreeUpdateHeight(self, node):
       leftHeight = -1
       if node.left != None:
           leftHeight = node.left.height
       rightHeight = -1
       if node.right != None:
           rightHeight = node.right.height
       node.height = max(leftHeight, rightHeight) + 1


    def AVLTreeSetChild(self, parent, whichChild, child):
        if whichChild != "left" and whichChild != "right":
          return False
  
        if whichChild == "left":
          parent.left = child
        else:
          parent.right = child
        if child != None:
          child.parent = parent
      
        self.AVLTreeUpdateHeight(parent)
        return True

    def AVLTreeReplaceChild(self, parent, currentChild, newChild):
        if parent.left == currentChild:
          return self.AVLTreeSetChild(parent, "left", newChild)
        elif parent.right == currentChild:
          return self.AVLTreeSetChild(parent, "right", newChild)
        return False

    def AVLTreeGetBalance(self, node):
        leftHeight = -1
        if node.left != None:
          leftHeight = node.left.height
        rightHeight = -1
        if node.right != None:
          rightHeight = node.right.height
        return leftHeight - rightHeight
    
    def AVLTreeRebalance(self, node):
        self.AVLTreeUpdateHeight(node)        
        if self.AVLTreeGetBalance(node) == -2:
            if self.AVLTreeGetBalance(node.right) == 1:
                self.AVLTreeRotateRight(node.right)
            return self.AVLTreeRotateLeft(node)
        elif self.AVLTreeGetBalance(node) == 2:
            if self.AVLTreeGetBalance(node.left) == -1:
                self.AVLTreeRotateLeft(node.left)
            return self.AVLTreeRotateRight(node)
        return node
    
    def AVLTreeInsert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
            node.parent = None
            return
        cur = self.root
        while cur != None:
            if node.key <= cur.key:
                if cur.left == None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        while node != None:
            self.AVLTreeRebalance(node)
            node = node.parent
        
    def AVLTreeRotateRight(self, node):
        leftRightChild = node.left.right
        if node.parent != None:
            self.AVLTreeReplaceChild(node.parent, node, node.left)
        else: #// node is root
            self.root = node.left
            self.root.parent = None
        self.AVLTreeSetChild(node.left, "right", node)
        self.AVLTreeSetChild(node, "left", leftRightChild)
    
    def AVLTreeRotateLeft(self, node):
        rightLeftChild = node.right.left
        if node.parent != None:
            self.AVLTreeReplaceChild(node.parent, node, node.right)
        else: #// node is root
            self.root = node.right
            self.root.parent = None
        self.AVLTreeSetChild(node.right, "left", node)
        self.AVLTreeSetChild(node, "right", rightLeftChild)

def BST_print (tree):
    cur = tree.root
    print(cur.key)
    BST_print_h(cur.left)
    BST_print_h(cur.right)
    
def BST_print_h(node):
    if node == None:
        return
    print(node.key)
    BST_print_h(node.left)
    BST_print_h(node.right)
    
def BST_search (tree, key):
    cur = tree.root
    while cur != None:
        if cur.key.lower() == key.lower():
            return True
        if key.lower() < cur.key.lower():
            cur = cur.left
        else:
            cur = cur.right
    return False

def count_anagrams (word, english_words, prefix = ""):
   if len(word) <= 1:
       str = prefix + word

       if BST_search(english_words, str):
           return 1
       return 0
   else:
       count = 0
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               count = count + count_anagrams(before + after, english_words, prefix + cur)
       return count
    
def print_anagrams (word, english_words, prefix = ""):
   if len(word) <= 1:
       str = prefix + word

       if BST_search(english_words, str):
           print(prefix + word)
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, prefix + cur)

def print_anagrams_b(word, english_words, prefix = ""):
    if len(word) <= 1:
        str = prefix + word
        
        if b_search(english_words, str):
            print(prefix + word)
    
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur

            if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams_b(before + after, english_words, prefix + cur)
               
def b_search(tree, word):
    cur = tree.root
    for i in range(len(cur.keys)):
        if cur.keys[i] > word:
            return b_search_h(cur.children[i], word)
    return b_search_h(cur.children[-1], word)

def b_search_h(node, word):
    if node.is_leaf:
        for i in range(len(node.keys)):
            if node.keys[i] == word:
                return True
        return False
        
    for i in range(len(node.keys)):
        if node.keys[i] > word:
            return b_search_h(node.children[i], word)
        elif node.keys[i] == word:
            return True
    return b_search_h(node.children[-1], word)

def main():
    forrest = []
    #forrest.append()
    file = open("C:\\Users\\Mikef\\Desktop\\Programs\\Classwork\\CS2302\\Lab 3 - Option B\\words.txt", 'r')
    degrees = input("How many degrees will the B-tree have?\n")
    print("Input recieved. \n Processing...")
    forrest.append(AVLBBST())
    forrest.append(BTree(int(degrees)))
    forrest.append(RedBlack())
    seed = file.readline().strip()
    sum_avl = 0
    sum_rb = 0
    sum_b = 0
    A = 0
    B = 0
    C = 0
    D = 0
    while seed != "":
        A = time.time()
        forrest[0].AVLTreeInsert(seed.lower())
        B = time.time()
        forrest[1].insert(seed.lower())
        C = time.time()
        forrest[2].rbInsert(seed.lower())
        D = time.time()
        seed = file.readline().strip()
        sum_avl += B - A
        sum_b += C - B
        sum_rb += D - C
    
    file.close()
    
    start_AV = time.time()
    print_anagrams("opt", forrest[0])
    end_AV = time.time()
    
    start_b = time.time()
    print_anagrams_b("opt", forrest[1])
    end_b = time.time()
    
    start_RB = time.time()
    print_anagrams("opt", forrest[2])
    end_RB = time.time()
    
    print("AVL runtime (Input): ", sum_avl)
    print("AVL runtime (Search): ", end_AV - start_AV)
    print("B-Tree runtime (Input): ", sum_b)
    print("B-Tree runtime (Search): ", end_b - start_b)
    print("Red Black runtime (Input): ", sum_rb)
    print("Red Black runtime (Search): ", end_RB - start_RB)
    
if __name__ == "__main__":
    main()
