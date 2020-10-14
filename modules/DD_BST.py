from modules import BST_Node


class DD_BST:
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

                if node.sorting_data < parent.sorting_data:
                    current = current.l_child
                    if current == None:
                        parent.l_child = node
                        return

                else:
                    current = current.r_child
                    if current == None:
                        parent.r_child = node
                        return

    def delete(self, key):
        parent = None

        current = self.root

        while current is not None and current.sorting_data != key:
            parent = current

            if key < current.sorting_data:
                current = current.l_child
            else:
                current = current.r_child

        if current is None:
            return None

        # case 1: no children: simple delete
        if current.l_child is None and current.r_child is None:
            if current != self.root:
                if parent.l_child == current:
                    parent.l_child = None
                else:
                    parent.r_child = None
            else:
                self.root = None

        # case 2: 2 children: replace node with next node in infix order and delete this next node
        elif current.l_child is not None and current.r_child is not None:
            successor = infix_successor(current.r_child)

            self.delete(successor.sorting_data)

            current.sorting_data = successor.sorting_data
            current.other_data = successor.other_data

        # case 3: 1 child: shift the sub-tree up by one
        else:
            child = ""
            if current.l_child:
                child = current.l_child
            else:
                child = current.r_child

            if current != self.root:
                if current == parent.l_child:
                    parent.l_child = child
                else:
                    parent.r_child = child
            else:
                self.root = child

        return current

    def __getitem__(self, value):
        if self.root is None:
            return [None]

        current = self.root

        while current is not None and current.sorting_data != value:
            if current != None:
                if current.sorting_data > value:
                    current = current.l_child
                else:
                    current = current.r_child

        if current is None:
            return [None]

        result = [current]

        # print("current: {}, current right: {}".format(current, current.r_child))

        over = False
        while not over:
            current = DD_BST(current.r_child).__getitem__(value)[0]
            if current:
                result.append(current)
            else:
                over = True

        # print(result)
        return result

    def __repr__(self):
        nodes = []
        return list_infix(self.root, nodes).__repr__()

    def balance(self):
        nodes_infix = []
        nodes_infix = list_infix(self.root, nodes_infix)
        self.root = sorted_array_to_BBST(nodes_infix)
        return

    def rebuild_index(self, nodes_infix):  # only use with BSTs with indexes as sorting_data
        i = 0
        for node in nodes_infix:
            node.sorting_data = i
            i += 1
        self.root = sorted_array_to_BBST(nodes_infix)
        return


def list_infix(root, nodes=[]):
    if root is None:
        return

    list_infix(root.l_child, nodes)
    nodes.append(BST_Node.Node(root.sorting_data, root.other_data))
    list_infix(root.r_child, nodes)

    return nodes


def infix_successor(root):
    if root is not None:
        current = root

        while current.l_child is not None:
            current = current.l_child

        return current

    return None


def list_postfix(root, nodes=[]):
    if root is None:
        return

    list_postfix(root.l_child, nodes)
    list_postfix(root.r_child, nodes)
    nodes.append(BST_Node.Node(root.sorting_data, root.other_data))

    return nodes


def list_prefix(root, nodes=[]):
    if root is None:
        return

    nodes.append(BST_Node.Node(root.sorting_data, root.other_data))
    list_prefix(root.l_child, nodes)
    list_prefix(root.r_child, nodes)

    return nodes


def sorted_array_to_BBST(array):
    if not array:
        return None

    mid = int((len(array)) / 2)
    # print(mid)

    root = array[mid]
    root.l_child = sorted_array_to_BBST(array[:mid])
    root.r_child = sorted_array_to_BBST(array[mid+1:])

    return root


""" 
#    TESTS

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
testbst.balance_and_rebuild_index()
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
 """
