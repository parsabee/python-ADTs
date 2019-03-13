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
from RedBlackTree import RBT_map

# a generic implementation of a map container, using a red black tree as its backbones

class orderedMap (object):
	def __init__ (self, cmpFxn = lambda x, y: 1 if x > y else (0 if x == y else -1)):
		self.__rbt = RBT_map(cmpFxn)
		self.__cmp = cmpFxn
		self.__size = 0
		self.__type = None

	def __contains__ (self, key):
		'''
		`in' and `not in' operators,
		returns true if key is in the map,
		false otherwise
		'''
		return self.__rbt.contains(key)

	def __str__ (self):
		'''
		returns the string representation of the in-order walk of the tree
		NB - User defined types should have the __str__ method defined as well
		'''
		return str(self.__rbt)

	def __repr__ (self):
		'''
		string representation of the ordered map object
		'''
		return 'orderedMap (size: {}, elements type: {})'.format(self.__size, self.__type)

	def __len__ (self):
		'''
		`len' function can be used to invoke this method
		returns the size of the map
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
		unions the current map with the second map (other)
		'''
		self.union(other)
		return self

	def __getitem__ (self, i):
		'''
		the [] operator for extracting the item at index i
		'''
		return self.__rbt.getVal(i)

	def __setitem__ (self, key, value):
		'''
		the [] operator for inserting value at index `key'
		'''
		return self.insert(key, value)

	def keys (self):
		'''
		returns a list of all the keys in the ordered map
		'''
		l = [ ]
		for i in self:
			l.append(i[0])
		return l

	def values (self):
		'''
		returns a list of all the values in the ordered map
		'''
		l = [ ]
		for i in self:
			l.append(i[1])
		return l

	def type (self):
		'''
		returns the type of elements in the map
		'''
		return self.__type

	def isEmpty (self):
		'''
		returns true if map is empty, false otherwise
		'''
		return self.__size == 0

	def insert (self, key, value):
		'''
		inserts a kay-value pair into the map
		updates the value if the key is already present
		'''
		if self.__size != 0:
			if self.__type != type(key):
				error = '{} is not of the same type as the keys of the map'\
					' {} != {}'.format(key, self.__type, type(key))
				raise TypeError(error)
		else:
			self.__type = type(key)

		pair = [key, value]
		status = self.__rbt.insert(pair)
		if status == 1:
			self.__size += 1
		return status

	def remove (self, key):
		'''
		removes a key and its associated value from the map
		returns 1 if successful
		0 if not (key doesn't exist in the map)
		'''
		if self.__size != 0:
			if self.__type != type(key):
				error = '{} is not of the same type as the elements of the map'\
					' {} != {}'.format(key, self.__type, type(key))
				raise TypeError(error)
		status = self.__rbt.delete(key)
		if status == 1:
			self.__size -= 1
		return status

	def union (self, other):
		'''
		unions the current map with the second map (other)
		'''
		if not isinstance (other, self.__class__):
			error = 'only an ordered map can be union\'d with the current map, '\
				'while {} is an object of type {}'.format(other, other.__type)
			raise TypeError(error)

		if self.__size != 0:
			if self.__type != other.__type:
				error = 'keys of the second map are not of the same type as this map'\
					' {} != {}'.format(self.__type, other.__type)
				raise TypeError(error)
		for i in other:
			self.__rbt.insert(i)

	def clear (self):
		'''
		clears all the elements of the map
		'''
		self.__rbt = RBT_map(self.__cmp)
		self.__size = 0
		self.__type = None

	def contains (self, key):
		'''
		same as `__contains__',
		returns true if key is in the map,
		false otherwise
		'''
		return self.__rbt.contains(key)

	def printMap (self, order = 'in-order', pretty = False):
		'''
		prints the elements of the map,
		this function performs the `in-order' walk on the binary search tree,
		if the pretty argument is set to True, the output will be in color 
		(i.e. the red nodes will be printed red, the black nodes will be printed black)
		'''
		if order != 'in-order' and order != 'pre-order' and order != 'post-order':
			raise ValueError('the order of traversals can only be the following:\n1) in-order\n2) pre-order\n3) post-order')
		self.__rbt.traverse(order, pretty)
