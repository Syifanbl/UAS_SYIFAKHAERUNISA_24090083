class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)

order_queue = Queue()
order_queue.enqueue("kentang")
order_queue.enqueue("Burger")
order_queue.enqueue("pizza")

print("Current orders:")
while not order_queue.is_empty():
    order = order_queue.dequeue()
    print(order)