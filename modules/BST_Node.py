class Node:
    def __init__(self, sorting_data, other_data, l_child=None, r_child=None):
        self.sorting_data = sorting_data
        self.other_data = other_data
        self.l_child = l_child
        self.r_child = r_child

    def __repr__(self):
        return "({0}, {1})".format(self.sorting_data, self.other_data)