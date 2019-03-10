__author__ = 'Matthew Hall'
'''
MIT License

Copyright (c) 2019, Parsa Bagheri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
'''
Modified by Parsa Bagheri
'''
class Node (object):
    def __init__(self, key, value = None, left = None, right = None, parent = None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __eq__(self, other):
        if other == None or self == None:
            return False
        return self.key == other.key

    def __iter__(self):
        # __iter__ defines an interator for objects of the RB_Node class
        # allows for operations like:
        # for node in Tree:
        # ... print( Tree.get(node) )

        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        return self.leftChild.parent == self and self.leftChild != self

    def hasRightChild(self):
        return self.rightChild.parent == self and self.rightChild != self

    def isLeftChild(self):
        return self.parent.leftChild == self and self.parent != self

    def isRightChild(self):
        return self.parent.rightChild == self and self.parent != self

    def findSuccessor(self):
        # successor's key is the next highest key from the current node

        succ = None
        # if node has a right child
        if self.hasRightChild():
            # then successor is the min of the right subtree
            succ = self.rightChild.findMin()
        elif self.parent: # node has no right child, but has a parent
            if self.isLeftChild(): # node is a left child
                succ = self.parent # then succ is the parent
            else: # node is right child, and has not right child
                # remove parent's rightChild reference
                self.parent.rightChild = None
                # recursively find call findSuccessor on parent
                succ = self.parent.findSuccessor()
                # replace parent's rightChild reference
                self.parent.rightChild = self
        return succ

    def findMin(self):
        # findMin travels across the leftChild of every node, and returns the
        # node who has no leftChild. This is the min value of a subtree

        currentNode = self
        while currentNode.hasLeftChild():
            currentNode = currentNode.leftChild
        return currentNode

class RB_Node (Node):
    def __init__(self, key, value = None, left = None, right = None, parent = None, color = 'red'):
        Node.__init__(self, key, value, left, right, parent)
        self.color = color

