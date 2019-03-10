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
from Heap import *
import sys

# A generic bounded priority queue container

class pQueue(object):
    '''
    bounded priority queue
    uses a heap data structure
    '''
    def __init__(self, size = 10, cmpFxn = lambda x,y: x > y) :
        '''
        two arguments:
        (1) size of the priority queue
            default is 10

        (2) compare function:
            compare function is used to determine the priority of inserted elements
            example of a compare function:
            def cmpFxn (x, y):
                return x > y

            function above is the defualt compare function, which produces a max heap

        NB - if you are making a priority queue to contain user defined types,
            you need to make sure that your compare function is capable of comapring the objects of that class
        '''
        self.__myHeap = Heap(size, cmpFxn)

    def __str__(self):
        '''
        prints the element of the queue

        NB To use this function, you need to make sure that the class of the object that is being inserted to the queue,
           has the __str__ method defined.
        '''
        return str(self.__myHeap)

    def __repr__ (self):
        '''
        string reprisentation of the priority queue object
        '''
        return 'pQueue (length: {}, elements type: {})'.format(self.__myHeap.getLength(), self.type())

    def __iter__ (self):
        '''
        itearator
        you can iterate through the queue by using `for i in queue'
        '''
        self.it = 1
        heap = self.__myHeap.getHeap()
        for i in range(1, self.__myHeap.getLength()+1):
            yield self.__myHeap.getHeap()[i]

    def __next__ (self):
        '''
        next operator used for the iterator
        '''
        if self.it < self.__myHeap.getLength():
            res = self.__myHeap.getHeap()[self.it]
            self.it += 1
            return res
        else:
            raise StopIteration

    def __contains__ (self, element):
        '''
        the `in' operator
        checks to see if element exists in the queue
        '''
        return element in self.__myHeap.getHeap()

    def __getitem__ (self, i):
        '''
        operator []
        returns the item at index i
        '''
        if i+1 > self.__myHeap.getLength():
            raise IndexError
        return self.__myHeap.getHeap()[i+1]

    def type (self):
        '''
        retunrs the type of elements in the queue
        '''
        return type(self.__myHeap.getHeap()[1])

    def setSize(self, size) :
        '''
        update the size of the queue,
        new size has to be greater than the old size
        if successful returns 1
        else (new size < old size) returns 0
        '''
        return self.__myHeap.setMaxSize(size)

    def getLength(self) :
        '''
        returns the number of elements in queue
        '''
        return self.__myHeap.getLength()
        
    def insert(self, data):
        '''
        inserts an element in the heap if there is room for insertion
        if successful returns 1
        else (queue is full) returns 0
        '''
        if self.getLength() != 0:
            if self.type() != type(data):
                error = '{} has a different type than the element of the pQueue'\
                    ' {} != {}'.format(data, type(data), self.type())
                raise TypeError (error)
        return self.__myHeap.insert(data)
        
    def top(self):
        '''
        returns the first element of the queue,
        None if the queue is empty
        '''
        return self.__myHeap.top()
    
    def pop(self):
        '''
        removes and returns the first element of the queue
        None if the queue is empty
        '''
        return self.__myHeap.extract()

    def isEmpty(self):
        '''
        returns True if the queue is empty, False otherwise
        '''
        return self.__myHeap.getLength() <= 1
    


    