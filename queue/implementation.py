class Queue (object):
    class Node (object):
        def __init__ (self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__ (self, *contents:list):
        self.__front = None
        self.__end = None
        self.__length = 0
        for content in contents:
            self.enqueue(content)

    def __len__ (self) -> int:
        return self.length

    def __repr__ (self) -> str:
        string_rep = "[ "
        node = self.__front
        while (True):
            string_rep += str(node.data)
            node = node.next
            if (node):
                string_rep += ", "
            else:
                break
        string_rep += " ]"
        return string_rep

    @property
    def length (self) -> int:
        return self.__length

    def enqueue(self, data) -> None:
        node = Queue.Node(data)
        if not self.__front:
            self.__front = node
        else:
            node.prev = self.__end
            self.__end.next = node
        self.__end = node
        self.__length += 1

    def dequeue (self):
        old_node = self.__front
        self.__front = old_node.next
        self.__front.prev = None
        old_node.next = None
        self.__length -= 1
        return old_node.data

    def peek (self):
        if (self.size):
            return self.__front.data
        raise Exception("Attempting to peek into an empty queue!")

if __name__ == "__main__":
    people = [
        "Mark Chan",
        "Jennifer Collins",
        "Spencer Wise"
    ]

    print("Constructing queue...")
    queue = Queue(*people)
    print("Queue:", queue)

    print("Adding item to queue...")
    queue.enqueue("Elijah Best")
    print("Queue:", queue)

    print("Removing item from queue...")
    print("item:", queue.dequeue())
    print("Queue:", queue)
