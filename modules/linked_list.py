class Linked_List:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        out_str = ""
        if self.root is None:
            return "linked list is empty"
        
        temp_node = self.root
        while temp_node is not None:
            out_str += "{0} => ".format(temp_node.data)
            temp_node = temp_node.next
        
        return out_str


    def insert(self, new_node, left_node=None):
        if left_node is None:
            left_node = self.last_node()
        if left_node is None:
            self.root = new_node
            return

        right_node = left_node.next
        left_node.next = new_node
        if right_node is not None:
            temp_node = new_node
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = right_node


    def delete(self, target_node=None):
        if target_node is None:
            target_node = self.last_node()

        left_node = self.find_parent(target_node)
        if left_node is None:
            self.root = target_node.next

            #TODO: fix delete function: does not delete yet

    def last_node(self):
        if self.root is None:
            return None

        temp_node = self.root
        while temp_node.next is not None:
            temp_node = temp_node.next

        return temp_node

    def find_parent(self, target_node):
        if self.root is None:
            return 0
        if self.root.next is None:
            return 1
        if self.root == target_node:
            return 2

        temp_node = self.root

        while temp_node.next is not None:
            if temp_node.next == target_node:
                return temp_node
            temp_node = temp_node.next

        raise NotInLinkedList()


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NotInLinkedList(Exception):
    def __init__(self):
        self.message = "Exception: target node not in linked list."
        super().__init__(self.message)


test1 = Linked_List()
node1 = Node(1)
node2 = Node(2)
node4 = Node(4)
node3 = Node(3, node4)

print(test1)
test1.insert(node1)
test1.insert(node2)
test1.insert(node3)
print(test1)
node5 = Node(5)
test1.delete(node1)
test1.delete(node2)
try:
    test1.delete(node5)
except:
    pass
print(test1)