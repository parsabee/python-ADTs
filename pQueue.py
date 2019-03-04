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

        NB if you are making a priority queue to contain user defined types,
            you need to make sure that your compare function is capable of comapring the objects of that class
        '''
        self.__myHeap = Heap(size, cmpFxn)

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
    
    def __str__(self):
        '''
        prints the element of the queue

        NB To use this function, you need to make sure that the class of the object that is being inserted to the queue,
           has the __str__ method defined.
        '''
        try:
            s = str(self.__myHeap)
            return ("Current Queue: " + s)
        except:
            print('the \'__str__\' method is not defined for the objects in the queue')
            return ''


    