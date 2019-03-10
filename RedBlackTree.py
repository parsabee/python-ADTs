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

class RBT (object):
    def __init__(self, cmpFxn):
        self._root = None
        self._sentinel = RB_Node(key = None, color = 'black')
        self._sentinel.parent = self._sentinel
        self._sentinel.leftChild = self._sentinel
        self._sentinel.rightChild = self._sentinel
        self._cmp = cmpFxn
        self._s = ''

    def __iter__(self):
        # in-order iterator for your tree
        return self._root.__iter__()

    def __str__ (self):
        self._walk_str('in-order', self._root)
        s = '{' + self._s[:len(self._s)-2] + '}'
        self._s = ''
        return s

    def getRoot (self):
        return self._root

    def contains(self, key) :
        tmp = self._root
        while tmp != self._sentinel and tmp != None:
            if self._cmp(tmp.key, key) == 0:
                return True
            if self._cmp(tmp.key, key) == 1:
                tmp = tmp.leftChild
            else:
                tmp = tmp.rightChild
        return False

    def __search(self, key) :

        tmp = self._root
        while tmp != self._sentinel and tmp != None:
            if self._cmp(tmp.key, key) == 0:
                return tmp
            if self._cmp(tmp.key, key) == 1:
                tmp = tmp.leftChild
            else:
                tmp = tmp.rightChild
        return None

    def getVal(self, key):
        n = self.__search(key)
        if n != None:
            return n.value
        return None

    def __newNode(self, key, value):
        return RB_Node(key = key, value = value, left = self._sentinel, right = self._sentinel, parent = self._sentinel)

    def insert(self, key, value = None):
        if self._root == None:
            self._root = self.__newNode(key, value)
            self._root.color = 'black'
            return 1
        p = None
        tmp = self._root
        while tmp != self._sentinel:
            p = tmp
            if self._cmp(key, tmp.key) == 0:
                return 0
            if self._cmp(key, tmp.key) == 1:
                tmp = tmp.rightChild                
            else:
                tmp = tmp.leftChild
        tmp = self.__newNode(key, value)
        if self._cmp(key, p.key) == 1:
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

        self._root.color = 'black'

    def delete(self, key):
        z = self.__search(key)
        if z == None:
            return 0
        if z.leftChild is self._sentinel or z.rightChild is self._sentinel:
            y = z
        else:
            y = z.findSuccessor()
        if y.leftChild is not self._sentinel:
            x = y.leftChild
        else:
            x = y.rightChild
        if x is not self._sentinel:
            x.parent = y.parent
        if y.parent is self._sentinel:
            p = self._root
            self._root = x
        else:
            p = y.parent
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x
        if y is not z:
            z.key = y.key
            z.value = y.value
        if y.color == 'black':
            self.__rb_delete_fixup(x, p)

        return 1

    def __rb_delete_fixup(self, x, y):
        while x != self._root and x.color == 'black':
            if x == y.leftChild:
                w = y.rightChild
                if w.color == 'red':
                    w.color = 'black'
                    y.color = 'red'
                    self.__leftRotate(y)
                    w = y.rightChild
                if w.leftChild.color == 'black' and w.rightChild.color == 'black':
                    if w != self._sentinel:
                        w.color = 'red'
                    x = y
                    y = y.parent
                else:
                    if w.rightChild.color == 'black':
                        w.leftChild.color = 'black'
                        if w != self._sentinel:
                            w.color = 'red'
                        self.__rightRotate(w)
                        w = y.rightChild
                    if w != self._sentinel:
                        w.color = y.color
                    w.rightChild.color = 'black'
                    y.color = 'black'
                    self.__leftRotate(y)
                    x = self._root
            else:
                w = y.leftChild
                if w.color == 'red':
                    w.color = 'black'
                    y.color = 'red'
                    self.__rightRotate(y)
                    w = y.leftChild
                if w.rightChild.color == 'black' and w.leftChild.color == 'black':
                    if w != self._sentinel:
                        w.color = 'red'
                    x = y
                    y = y.parent
                else:
                    if w.leftChild.color == 'black':
                        w.rightChild.color = 'black'
                        if w != self._sentinel:
                            w.color = 'red'
                        self.__leftRotate(w)
                        w = y.leftChild
                    if w != self._sentinel:
                        w.color = y.color
                    w.leftChild.color = 'black'
                    y.color = 'black'
                    self.__rightRotate(y)
                    x = self._root
        x.color = 'black'

    def traverse(self, order, pretty) :
        self._walk(order, self._root, pretty)
        sys.stdout.write('\033[m\n')

    def _walk(self, order, top, pretty):
        if top != self._sentinel :
            if order == "in-order":
                self._walk("in-order", top.leftChild, pretty)
                self._pretty_print(top, pretty)
                self._walk("in-order", top.rightChild, pretty)

            if order == "pre-order":
                self._pretty_print(top, pretty)
                self._walk( "pre-order", top.leftChild, pretty)
                self._walk( "pre-order", top.rightChild, pretty)

            if order == "post-order":
                self._walk("post-order", top.leftChild, pretty)
                self._walk("post-order", top.rightChild, pretty)
                self._pretty_print(top, pretty)

    def _walk_str(self, order, top):
        if top != self._sentinel:
            self._walk_str("in-order", top.leftChild)
            self._s += str(top.key) + ', '
            self._walk_str("in-order", top.rightChild)

    def _pretty_print(self, n, pretty):
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
        if y.leftChild != self._sentinel:
            y.leftChild.parent = x
        y.parent = x.parent
        if x.parent == self._sentinel:
            self._root = y
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
        if y.rightChild != self._sentinel:
            y.rightChild.parent = x
        y.parent = x.parent
        if x.parent == self._sentinel:
            self._root = y
        elif x == x.parent.rightChild:
            x.parent.rightChild = y
        else:
            x.parent.leftChild = y
        y.rightChild = x
        x.parent = y

class RBT_map (RBT):
    def _walk_str(self, order, top):
        if top != self._sentinel:
            self._walk_str("in-order", top.leftChild)
            self._s += str(top.key) + ': ' + str(top.value) + ', '
            self._walk_str("in-order", top.rightChild)

    def _pretty_print(self, n, pretty):
        if pretty:
            if n.color == 'red':
                sys.stdout.write('\033[1;31m{}: {} '.format(n.key, n.value))
            else:
                sys.stdout.write('\033[1;30m{}: {} '.format(n.key, n.value))
        else:
            sys.stdout.write(str(n.key) + ' ')

