class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        current = None
        parent = None

        if self.root == None:
            self.root = node
        else:
            current = self.root

            while(True):
                parent = current

                if node.index < parent.index:
                    current = current.l_child
                    if current == None:
                        parent.l_child = node
                        return

                else:
                    current = current.r_child
                    if current == None:
                        parent.r_child = node
                        return

    def __getitem__(self, value):
        if self.root is None:
            return None

        current = self.root

        while current.index != value:
            if current != None:
                if current.index > value:
                    current = current.l_child
                else:
                    current = current.r_child

            if current == None:
                return None

        return current

    def balance(self):
        nodes_infix = []
        nodes_infix = list_infix(self.root, nodes_infix)
        for node in nodes_infix:
            print(node, end=", ")
        print()
        self.root = sorted_array_to_BBST(nodes_infix)
        return


class Node:
    def __init__(self, index, data, l_child=None, r_child=None):
        self.index = index
        self.data = data
        self.l_child = l_child
        self.r_child = r_child

    def __str__(self):
        return "({0}, {1})".format(self.index, self.data)


def list_infix(root, nodes=[]):
    if root is None:
        return

    list_infix(root.l_child, nodes)
    nodes.append(Node(root.index, root.data))
    list_infix(root.r_child, nodes)

    return nodes


def list_postfix(root, nodes=[]):
    if root is None:
        return

    list_postfix(root.l_child, nodes)
    list_postfix(root.r_child, nodes)
    nodes.append(Node(root.index, root.data))

    return nodes


def list_prefix(root, nodes=[]):
    if root is None:
        return

    nodes.append(Node(root.index, root.data))
    list_prefix(root.l_child, nodes)
    list_prefix(root.r_child, nodes)

    return nodes


def sorted_array_to_BBST(array):

    if not array:
        return None

    # find middle
    mid = int((len(array)) / 2)
    # print(mid)

    # make the middle element the root
    root = array[mid]

    # left subtree of root has all
    # values < arr[mid]
    root.l_child = sorted_array_to_BBST(array[:mid])

    # right subtree of root has all
    # values > arr[mid]
    root.r_child = sorted_array_to_BBST(array[mid+1:])

    return root


testbst = BST()
print(testbst[0])
print("=================")
node1 = Node(0, "a")
node2 = Node(1, "a")
node3 = Node(2, "a")
node4 = Node(3, "a")
node5 = Node(6, "a")
node6 = Node(-5, "a")

testbst.insert(node1)
testbst.insert(node2)
testbst.insert(node3)
testbst.insert(node4)
testbst.insert(node5)
testbst.insert(node6)

print("infix")
bst_infix_1 = []
list_infix(testbst.root, bst_infix_1)
for node in bst_infix_1:
    print(node, end=", ")
print()

print("prefix")
bst_prefix_1 = []
list_prefix(testbst.root, bst_prefix_1)
for node in bst_prefix_1:
    print(node, end=", ")
print()
print("=================")

print(testbst[0])
print(testbst[4])
print(testbst[5])

print("=================")
print("balance")
testbst.balance()
print("infix")
bst_infix_1 = []
list_infix(testbst.root, bst_infix_1)
for node in bst_infix_1:
    print(node, end=", ")
print()

print("prefix")
bst_prefix_1 = []
list_prefix(testbst.root, bst_prefix_1)
for node in bst_prefix_1:
    print(node, end=", ")
print()
print("=================")
