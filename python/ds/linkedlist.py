class LinkedList(object):
    """Summary of class here.

    outer class: LinkedList
    inner class: _Node

    """
    class _Node(object):
        """Summary of class here.

        This is a inner class which is invisible to the outside

        """
        def __init__(self, item, next_node=None):
            self.item = item
            self.next = next_node

        def get_item(self):
            return self.item

        def get_next(self):
            return self.next

        def set_item(self, item):
            self.item = item

        def set_next(self, next_node):
            self.next = next_node

    def __init__(self, contents=None):
        self.first = LinkedList._Node(None, None)
        self.last = self.first
        self.num_items = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()

            return cursor.get_item()

        raise IndexError('LinkedList index out of range')

    def __setitem__(self, index, val):
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()

            cursor.set_item(val)
            return

        raise IndexError('LinkedList index out of range')

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError('Concatenate undefined for {} + {}'.format(
                str(type(self)), str(type(other))))

        result = LinkedList()
        cursor = self.first.get_next()

        while cursor != None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()

        cursor = other.first.get_next()

        while cursor != None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()

        return result

    def append(self, item):
        node = LinkedList._Node(item)
        self.last.set_next(node)
        self.last = node
        self.num_items += 1

    def insert(self, index, item):
        cursor = self.first

        if index < self.num_items:
            for i in range(index):
                cursor = cursor.get_next()

            node = LinkedList._Node(item, cursor.get_next())
            cursor.set_next(node)
            self.num_items += 1
        else:
            self.append(item)
