class LinkedList (object):
    class OutOfBoundsError (Exception):
        def __init__ (self, i):
            super().__init__(i)
            self.message = "The index {i} is out of bounds"

    class Node (object):
        def __init__ (self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__ (self, *data):
        self.head = None
        self.tail = None
        self.length = 0
        for datum in data:
            self.push(datum)

    def __str__ (self):
        string = "[ "
        node = self.head
        while (node != None):
            string += str(node.data)
            if (node.next != None):
                string += " <-> "
            node = node.next
        string += " ]"
        return string

    def clear (self):
        self.head = None
        self.length = 0
        return self

    def peek (self, index):
        if (index >= self.length):
            raise LinkedList.OutOfBoundsError(index)

        i = 0
        node = self.head
        while (i < index):
            node = node.next
            i += 1
        return node.data

    def pop (self, index):
        if (index >= self.length):
            raise LinkedList.OutOfBoundsError(index)
        self.length -= 1
        if (index == 0):
            self.head.next.prev = self.head.prev
            node = self.head
            self.head = self.head.next
            return self.head
        i = 0
        node = self.head
        while (i < index):
            node = node.next
            i += 1
        node.prev.next = node.next
        if (node.next):
            node.next.prev = node.prev
        return node.data

    def push (self, data):
        if (not self.length):
            self.head = self.tail = LinkedList.Node(data)
        else:
            new_node = LinkedList.Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def insert (self, index, data):
        if (index > self.length or index < 0):
            raise LinkedList.OutOfBoundsError(index)
        self.length += 1
        new_node = LinkedList.Node(data)
        if (index == 0):
            if (self.head):
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
            else:
                self.head = self.tail = new_node
            return self
        node = self.head
        i = 0
        while (i < index):
            node = node.next
            i += 1
        if (node == None):
            return self.push(data)
        node.prev.next = new_node
        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node
        return self

    def remove (self, data):
        node = self.head
        while (node != None):
            if (node.data == data):
                node.prev.next = node.next
                if (node.next):
                    node.next.prev = node.prev
                self.length -= 1
                return self
            node = node.next
        raise ValueError(f"'{data}' is not in the linked list")

if __name__ == "__main__":
    data = [
        "man",
        "woman",
        "boy",
        "girl"
    ]

    print("Creating linked list...", end = " ")
    llist = LinkedList()
    llist.push(data[0])
    llist.push(data[2])
    print(llist)
    print("Clearing linked list...", end = " ")
    print(llist.clear())

    print("\nCreating linked list...", end = " ")
    llist = LinkedList(*data)
    print(llist)
    print("Peeking at index 1 =", llist.peek(1))
    print("Popping index 1...", end = " ")
    llist.pop(1) # returns woman
    print(llist)
    print("Peeking at index 1 =", llist.peek(1))
    print("Removing 'boy' from the list =", llist.remove("boy"))
    print("Inserting 'woman' at index 1...", llist.insert(1, "woman"))
    print("Inserting 'boy' at index 3...", llist.insert(3, "boy"))
    print("Clearing linked list...", end = " ")
    print(llist.clear())
    print("Inserting 'girl' to the list...", llist.insert(0, "girl"))
    print("Pushing 'woman' to the list...", llist.push("woman"))
