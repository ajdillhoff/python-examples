class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        """Let the string representation of the data do the work."""
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def __str__(self):
        """Return a string representation of the linked list."""
        if self.head is None:
            return '[]'
        else:
            current = self.head
            output = '['
            while current is not None:
                output += f'{current.data}, '
                current = current.next
            return output[:-2] + ']'

    def __len__(self):
        """Return the number of items in the linked list."""
        return self.count
    
    def __getitem__(self, index):
        """Return the item at the given index."""
        if index < 0 or index >= self.count:
            raise IndexError('Index out of bounds')
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data
        
    def __setitem__(self, index, value):
        """Set the item at the given index to the given value."""
        if index < 0 or index >= self.count:
            raise IndexError('Index out of bounds')
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.data = value

    def __contains__(self, item):
        """Return whether or not the given item is in the linked list."""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def __iter__(self):
        """Return an iterator for the linked list."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def append(self, item):
        """Add the given item to the end of the linked list."""
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1

    def prepend(self, item):
        """Add the given item to the beginning of the linked list."""
        node = Node(item)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.count += 1
    
    def insert(self, index, item):
        """Insert the given item at the given index."""
        if index < 0 or index > self.count:
            raise IndexError('Index out of bounds')
        elif index == 0:
            self.prepend(item)
        elif index == self.count:
            self.append(item)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node = Node(item)
            node.next = current.next
            current.next = node
            self.count += 1

    def remove(self, item):
        """Remove the given item from the linked list."""
        if self.head is None:
            raise ValueError('Item not found')
        elif self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.count -= 1
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == item:
                    current.next = current.next.next
                    if current.next is None:
                        self.tail = current
                    self.count -= 1
                    return
                current = current.next
            raise ValueError('Item not found')
        
    def pop(self, index=None):
        """Remove and return the item at the given index."""
        if index is None:
            index = self.count - 1
        if index < 0 or index >= self.count:
            raise IndexError('Index out of bounds')
        elif index == 0:
            item = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.count -= 1
            return item
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            item = current.next.data
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self.count -= 1
            return item
        
    def clear(self):
        """Remove all items from the linked list."""
        self.head = None
        self.tail = None
        self.count = 0

    def index(self, item):
        """Return the index of the given item."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError('Item not found')
    
    def reverse(self):
        """Reverse the linked list."""
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def copy(self):
        """Return a copy of the linked list."""
        copy = LinkedList()
        current = self.head
        while current is not None:
            copy.append(current.data)
            current = current.next
        return copy
    
    def count(self, item):
        """Return the number of times the given item appears in the linked list."""
        count = 0
        current = self.head
        while current is not None:
            if current.data == item:
                count += 1
            current = current.next
        return count
    
    def extend(self, other):
        """Add all items from the other linked list to this linked list."""
        current = other.head
        while current is not None:
            self.append(current.data)
            current = current.next
        
    def is_empty(self):
        """Return whether or not the linked list is empty."""
        return self.head is None