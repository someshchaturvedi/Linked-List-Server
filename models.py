class LinkedListManager(object):
    linked_lists = {}
    count = 0

    def add(self):
        self.linked_lists[100 + self.count] = LinkedList(100 + self.count)
        self.count = self.count + 1

    def delete(self, id):
        del self.linked_lists[id]

class LinkedList(object):
    def __init__(self, id):
        self.id = id
