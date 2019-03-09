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
from RedBlackTree import RBT

# a generic ordered set container implementing a red black tree

class orderedSet(object):
	def __init__ (self, cmpFxn = lambda x, y: 1 if x > y else (0 if x == y else -1)):
		'''
		this ordered set uses a red black tree structure.
		red black tree is an efficiant choice, because of the better amortized asymptotic complexity of insert and delete (O(log n))
		initializer takes one argument:
		(1) cmpFxn:
			the compare function is used to determine the order of the elements being inserted,
			the function must return 0 if first==second, -1 if first<second, and 1 if first>second
			
			NB - there is a default compare function for generic types,
			however the user is responsible for providing a compare function for user defined types

		'''
		self.__rbt = RBT(cmpFxn)
		self.__cmp = cmpFxn
		self.__size = 0

	def __contains__ (self, element):
		'''
		`in' and `not in' operators,
		returns true if element is in the set,
		false otherwise
		'''
		return self.__rbt.contains(element)

	def __str__ (self):
		'''
		returns the string representation of the in-order walk of the tree
		NB - User defined types should have the __str__ method defined as well
		'''
		return str(self.__rbt)

	def __repr__ (self):
		'''
		string reprisentation of the ordered set object
		'''
		return 'orderedSet, size: {}'.format(self.__size)

	def __len__ (self):
		'''
		`len' function can be used to invoke this method
		returns the size of the set
		'''
		return self.__size

	def __iter__ (self):
		'''
		the iterator operator,
		the elements can be iterated over through `for i in orderedSet'
		'''
		return self.__rbt.__iter__()

	def __add__ (self, other):
		'''
		the + operator,
		unions the current set with the second set (other)
		'''
		if not isinstance (other, self.__class__):
			raise TypeError('only an ordered set can be union\'d with the current set, '\
				'while you are trying to union an object of type {}'.format(type(other)))
		for i in other:
			self.__rbt.insert(i)
		return self

	def isEmpty (self):
		'''
		returns true if set is empty, false otherwise
		'''
		return self.__size == 0

	def insert (self, element):
		'''
		inserts an element into the set
		returns 1 if successful
		0 if not (element already is in the set)
		'''
		status = self.__rbt.insert(element)
		if status == 1:
			self.__size += 1
		return status

	def remove (self, element):
		'''
		removes an element from the set
		returns 1 if successful
		0 if not (element doesn't exist in the set)
		'''
		status = self.__rbt.delete(element)
		if status == 1:
			self.__size -= 1
		return status

	def union (self, other):
		'''
		same as __add__
		unions the current set with the second set (other)
		'''
		if not isinstance (other, self.__class__):
			raise TypeError('only an ordered set can be union\'d with the current set, '\
				'while you are trying to union an object of type {}'.format(type(other)))
		for i in other:
			self.__rbt.insert(i)

	def clear (self):
		'''
		clears all the elements of the set
		'''
		self.__rbt = RBT(self.__cmp)
		self.__size = 0

	def contains (self, element):
		'''
		same as `__contains__',
		returns true if element is in the set,
		false otherwise
		'''
		return self.__rbt.contains(element)

	def print_set (self, order = 'in-order', pretty = False):
		'''
		prints the elements of the set,
		this function performs the `in-order' walk on the binary search tree,
		if the pretty argument is set to True, the output will be in color 
		(i.e. the red nodes will be printed red, the black nodes will be printed black)
		'''
		if order != 'in-order' and order != 'pre-order' and order != 'post-order':
			raise ValueError('the order of traversals can only be the following:\n1) in-order\n2) pre-order\n3) post-order')
		self.__rbt.traverse(order, pretty)


