class LinkedListManager(object):
    linked_lists = {}
    count = 0

    def create_list(self, name, birthyear):
        new_id = str(100 + self.count + 1)
        linked_list = LinkedList(name, birthyear)
        linked_list._id = new_id
        self.linked_lists[new_id] = linked_list
        self.count = self.count + 1
        return linked_list

    def retrieve_list(self, id):
        if id not in self.linked_lists.keys():
            return None
        return self.linked_lists[id]

    def delete(self, id):
        if id not in self.linked_lists.keys():
            return None
        return self.linked_lists[id]
        del self.linked_lists[id]

class LinkedList(object):
    length = 0
    _id = 0
    new_node_id = 1
    head = None
    curr = None
    def __init__(self, name, birthyear):
        self.add_node(name, birthyear)
    
    def add_node(self, name, birthyear):
        new_id = self.new_node_id
        new_node = Node(new_id, name, birthyear)
        if self.curr is not None:
            self.curr.next = new_node
            new_node.prev = self.curr
        self.curr = new_node
        self.length = self.length + 1
        self.new_node_id = self.new_node_id + 1
        if self.head is None:
            self.head = new_node

    def to_json(self):
        all_nodes = self.get_nodes()
        data = {'meta': {'id': self._id, 'length': self.length},
            'object': [node.to_json() for node in all_nodes]
        }
        return data
    
    def pop_node(self):
        if self.length == 0:
            return
        if self.curr == self.head:
            self.head = None
        self.curr = self.curr.prev
        if self.curr:
            self.curr.next = None
        self.length = self.length - 1

    def remove_node(self, name, birthyear):
        i = self.head
        while i is not None:
            if i.name == name and i.birthyear == birthyear:
                if i == self.head: self.head = self.head.next
                if i.prev is not None: i.prev.next = i.next
                if i.next is not None: i.next.prev = i.prev
                self.length = self.length - 1
                return i
            i = i.next
        return None
    
    def reverse(self):
        temp = None
        current = self.head 
        self.curr = self.head
        while current is not None: 
            temp = current.prev  
            current.prev = current.next
            current.next = temp 
            current = current.prev 

        if temp is not None: 
            self.head = temp.prev

    def get_nodes(self):
        i = self.head
        nodes = []
        while(i is not None):
            nodes.append(i)
            i = i.next
            print(i)
        return nodes
    
class Node(object):
    _id = 0
    next = None
    prev = None
    def __init__(self, new_id, name, birthyear):
        self._id = new_id
        self.name = name
        self.birthyear = birthyear
    
    def to_json(self):
        data = {
            'id': self._id,
            'name': self.name,
            'birthyear': self.birthyear,
            'next': str(self.next)
        }
        return data
    
    def __str__(self):
        return str(self._id)
