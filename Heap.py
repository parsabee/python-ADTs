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

# A Generic container that uses the heap datastructure
# It will be used to create priority queues

class Heap(object):
    def __init__(self, size, cmpFxn):
        self.__maxSize = size
        self.__length = 0
        self.__heap = [None] * (size + 1)
        self.__cmp = cmpFxn

    def __str__ (self):
        s = ""
        for i in range (1, self.__length):
            s += str(self.__heap[i])
            s += ", "
        s += str(self.__heap[self.__length])
        return s

    def getHeap(self):
        return self.__heap

    def getMaxSize(self):
        return self.__maxSize
    
    def setMaxSize(self, ms):
        if ms <= self.__maxSize:
            return 0
        new_heap = [None] * (ms - self.__maxSize)
        self.__heap += new_heap
        self.__maxSize = ms
        return 1

    def getLength(self):
        return self.__length

    def __getParent(self, i):
        assert i >= 1
        if i == 1:
            return 1
        return i//2

    def __getLeft(self, i):
        return i * 2

    def __getRight(self, i):
        return (i * 2) + 1

    def __swap(self, i, j):
        tmp = self.__heap[i]
        self.__heap[i] = self.__heap[j]
        self.__heap[j] = tmp

    def insert(self, data):
        try:
            self.__length += 1
            if self.__length > self.__maxSize:
                self.__length -= 1
                return 0
            self.__heap [self.__length] = data
            i = self.__length
            ip = self.__getParent(i)
            while self.__cmp(self.__heap[i], self.__heap[ip]):
                self.__swap(i, ip)
                i = ip
                ip = self.__getParent(ip)
            return 1
        except:
            print('there is no way to comare the inserted objects\n' \
                'suggestion: either objects of different types are being inserted or\n' \
                'you may need to define the \'__eq__\' and \'__lt__\' operators for the class of the object you are inserting')
            self.__heap [self.__length] = None
            self.__length -= 1
            return 0

    def top(self):
        if self.__length < 1:
            return None
        return self.__heap[1]

    def extract(self):
        if self.__length < 1:
            return None
        r = self.__heap[1]
        self.__swap(1, self.__length)
        self.__heap[self.__length] = None
        self.__length -= 1
        if self.__length > 1:
            self.__heapify()
        return r

    def __heapify(self):
        n = 1
        while n < self.__length:
            l = self.__getLeft(n)
            r = self.__getRight(n)
            try:
                rp = l
                if self.__heap[r] != None:
                    if self.__cmp(self.__heap[r], self.__heap[l]):
                        rp = r
                if rp > self.__length:
                    break
            except IndexError:
                break
                    
            if self.__cmp(self.__heap[rp], self.__heap[n]):
                self.__swap(rp, n)
                n = rp
            else:
                break