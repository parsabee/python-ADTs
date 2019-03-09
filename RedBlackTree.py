__author__ = 'Parsa Bagheri'
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
from Node import RB_Node
import sys

class RBT:
    def __init__(self, cmpFxn):
        self.__root = None
        self.__sentinel = RB_Node(key = None, color = 'black')
        self.__sentinel.parent = self.__sentinel
        self.__sentinel.leftChild = self.__sentinel
        self.__sentinel.rightChild = self.__sentinel
        self.__cmp = cmpFxn
        self.__s = ''

    def __iter__(self):
        # in-order iterator for your tree
        return self.__root.__iter__()

    def __str__ (self):
        self.__walk_str('in-order', self.__root)
        s = '{' + self.__s[:len(self.__s)-2] + '}'
        self.__s = ''
        return s

    def contains(self, key) :
        tmp = self.__root
        while tmp != self.__sentinel and tmp != None:
            if self.__cmp(tmp.key, key) == 0:
                return True
            if self.__cmp(tmp.key, key) == 1:
                tmp = tmp.leftChild
            else:
                tmp = tmp.rightChild
        return False

    def __search(self, key) :

        tmp = self.__root
        while tmp != self.__sentinel and tmp != None:
            if self.__cmp(tmp.key, key) == 0:
                return tmp
            if self.__cmp(tmp.key, key) == 1:
                tmp = tmp.leftChild
            else:
                tmp = tmp.rightChild
        return None

    def __newNode(self, key):
        return RB_Node(key, self.__sentinel, self.__sentinel, self.__sentinel)

    def insert(self, key):
        if self.__root == None:
            self.__root = self.__newNode(key)
            self.__root.color = 'black'
            return 1
        p = None
        tmp = self.__root
        while tmp != self.__sentinel:
            p = tmp
            if self.__cmp(key, tmp.key) == 0:
                return 0
            if self.__cmp(key, tmp.key) == 1:
                tmp = tmp.rightChild                
            else:
                tmp = tmp.leftChild
        tmp = self.__newNode(key)
        if self.__cmp(key, p.key):
            p.rightChild = tmp
        else:
            p.leftChild = tmp
        tmp.parent = p
        self.__rb_insert_fixup(tmp)
        return 1

    def __rb_insert_fixup(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.leftChild:
                y = z.parent.parent.rightChild
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.rightChild:
                        z = z.parent
                        self.__leftRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.__rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.leftChild
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.leftChild:
                        z = z.parent
                        self.__rightRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.__leftRotate(z.parent.parent)

        self.__root.color = 'black'

    def delete(self, key):
        z = self.__search(key)
        if z == None:
            return 0
        if z.leftChild is self.__sentinel or z.rightChild is self.__sentinel:
            y = z
        else:
            y = z.findSuccessor()
        if y.leftChild is not self.__sentinel:
            x = y.leftChild
        else:
            x = y.rightChild
        if x is not self.__sentinel:
            x.parent = y.parent
        if y.parent is self.__sentinel:
            p = self.__root
            self.__root = x
        else:
            p = y.parent
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x
        if y is not z:
            z.key = y.key
        if y.color == 'black':
            self.__rb_delete_fixup(x, p)

        return 1

    def __rb_delete_fixup(self, x, y):
        while x != self.__root and x.color == 'black':
            if x == y.leftChild:
                w = y.rightChild
                if w.color == 'red':
                    w.color = 'black'
                    y.color = 'red'
                    self.__leftRotate(y)
                    w = y.rightChild
                if w.leftChild.color == 'black' and w.rightChild.color == 'black':
                    if w != self.__sentinel:
                        w.color = 'red'
                    x = y
                    y = y.parent
                else:
                    if w.rightChild.color == 'black':
                        w.leftChild.color = 'black'
                        if w != self.__sentinel:
                            w.color = 'red'
                        self.__rightRotate(w)
                        w = y.rightChild
                    if w != self.__sentinel:
                        w.color = y.color
                    w.rightChild.color = 'black'
                    y.color = 'black'
                    self.__leftRotate(y)
                    x = self.__root
            else:
                w = y.leftChild
                if w.color == 'red':
                    w.color = 'black'
                    y.color = 'red'
                    self.__rightRotate(y)
                    w = y.leftChild
                if w.rightChild.color == 'black' and w.leftChild.color == 'black':
                    if w != self.__sentinel:
                        w.color = 'red'
                    x = y
                    y = y.parent
                else:
                    if w.leftChild.color == 'black':
                        w.rightChild.color = 'black'
                        if w != self.__sentinel:
                            w.color = 'red'
                        self.__leftRotate(w)
                        w = y.leftChild
                    if w != self.__sentinel:
                        w.color = y.color
                    w.leftChild.color = 'black'
                    y.color = 'black'
                    self.__rightRotate(y)
                    x = self.__root
        x.color = 'black'

    def traverse(self, order, pretty) :
        self.__walk(order, self.__root, pretty)
        sys.stdout.write('\033[m\n')

    def __walk(self, order, top, pretty):
        if top != self.__sentinel :
            if order == "in-order":
                self.__walk("in-order", top.leftChild, pretty)
                self.__pretty_print(top, pretty)
                self.__walk("in-order", top.rightChild, pretty)

            if order == "pre-order":
                self.__pretty_print(top, pretty)
                self.__walk( "pre-order", top.leftChild, pretty)
                self.__walk( "pre-order", top.rightChild, pretty)

            if order == "post-order":
                self.__walk("post-order", top.leftChild, pretty)
                self.__walk("post-order", top.rightChild, pretty)
                self.__pretty_print(top, pretty)

    def __walk_str(self, order, top):
        if top != self.__sentinel:
            self.__walk_str("in-order", top.leftChild)
            self.__s += str(top.key) + ', '
            self.__walk_str("in-order", top.rightChild)

    def __pretty_print(self, n, pretty):
        if pretty:
            if n.color == 'red':
                sys.stdout.write('\033[1;31m{} '.format(n.key))
            else:
                sys.stdout.write('\033[1;30m{} '.format(n.key))
        else:
            sys.stdout.write(str(n.key) + ' ')

    def __leftRotate(self, x):
        # perform a left rotation from a given node
        y = x.rightChild
        x.rightChild = y.leftChild
        if y.leftChild != self.__sentinel:
            y.leftChild.parent = x
        y.parent = x.parent
        if x.parent == self.__sentinel:
            self.__root = y
        elif x == x.parent.leftChild:
            x.parent.leftChild = y
        else:
            x.parent.rightChild = y
        y.leftChild = x
        x.parent = y

    def __rightRotate(self, x):
        # perform a right rotation from a given node
        y = x.leftChild
        x.leftChild = y.rightChild
        if y.rightChild != self.__sentinel:
            y.rightChild.parent = x
        y.parent = x.parent
        if x.parent == self.__sentinel:
            self.__root = y
        elif x == x.parent.rightChild:
            x.parent.rightChild = y
        else:
            x.parent.leftChild = y
        y.rightChild = x
        x.parent = y
         