from ListNode import ListNode 

class MyList:

	def __init__(self):
		self._count = 0
		self._head = None
		self._current = None


	def add(self, newNode):
		"""add an item into the list."""
		if self._head == None:
			self._head = newNode
			self._current = self._head
		else:
			self._current._next = newNode
			self._current = self._current._next
		self._count += 1

	def count(self):
		"""return the item(s) number in this list"""
		return self._count

	def delete(self, position):
		"""delete the n-th item (n = position)"""
		if position < 0:
			raise ValueError("wrong value.")
		if position >= self._count:
			raise OverflowError("position is too big.")
		if position == 0:
			temp = self._head._next
			self._head._next = None
			self._head = temp
			self._count = 0
		else:
			temp = self._head
			for x in xrange(1, position):
				temp = temp._next
			temp2 = temp._next
			temp._next = temp2._next
			temp2._next = None
		self._count -= 1

	def update(self, position, data):
		"""update the n-th item (n = position)"""
		if position < 0:
			raise ValueError("wrong value.")
		if position >= self._count:
			raise OverflowError("position is too big.")
		
		temp = self._head
		for x in xrange(0, position):
			temp = temp._next
		temp._data = data

	def get(self, position):
		"""update the n-th item (n = position)"""
		if position < 0:
			raise ValueError("wrong value.")
		if position >= self._count:
			raise OverflowError("position is too big.")
		
		temp = self._head
		for x in xrange(0, position):
			temp = temp._next
		return temp._data

	def showAll(self):
		"""print all the item(s) in order."""
		temp = self._head
		while(temp != None):
			print(temp._data)
			temp = temp._next


def main():
	list = MyList()
	for x in xrange(1,10):
		newNode = ListNode(x)
		list.add(newNode)
	list.update(3, 1000)
	#list.delete(0)
	#list.delete(3)
	list.delete(8)
	list.showAll()
	print list.get(4)

main()