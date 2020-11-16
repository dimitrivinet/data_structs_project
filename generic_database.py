
from collections import OrderedDict

import modules
import numpy as np
import time

table_list = {}

def create_table(name, table_object):
    table_list[name] = table_object
    return table_object

class Table:
    # table is ordered dict with {attribute name: list of attribute characteristics (type, max length, isPrimaryKey)}
    def __init__(self, **attributes):
        self.attributes = OrderedDict()
        self.max_index = 0
        self.primary_key = ""

        for key, value in attributes.items():
            self.attributes[key] = value
            try:
                self.primary_key = value[2]
                self.primary_key = key
            except:
                pass

        self.attributes_keys = list(self.attributes.keys())
        # print(self.attributes_keys)
        self.members = modules.DD_BST.DD_BST()

        self.indexed_members = OrderedDict()

        for attribute in self.attributes_keys:
            self.indexed_members[attribute] = modules.DD_BST.DD_BST()
        # print(self.indexed_members)

    def insert(self, *attributes):
        if len(attributes) == len(self.attributes):  # if the list supplied is the correct length

            for i in range(len(self.attributes)):  # for each attribute of the table

                if type(attributes[i]) is self.attributes[self.attributes_keys[i]][0]:  # check if type is correct

                    if type(attributes[i]) is str:  # if the attribute is a string, check if the length is correct
                        if len(attributes[i]) <= self.attributes[self.attributes_keys[i]][1]:
                            pass
                    elif type(attributes[i]) is int:  # if the attribute is an int, check if value is under max value (when only length is supplied in attribute definition)
                        if attributes[i] <= 10**(self.attributes[self.attributes_keys[i]][1] + 1):
                            pass

                    else:
                        raise modules.exceptions.InvalidAttributeLength(attributes[i], len(attributes[i]))

                else:  # if attribute type is incorrect
                    raise modules.exceptions.InvalidAttributeType(attributes[i], type(attributes[i]))

            member = np.array(attributes)
            # print(member)

            self.members.insert(modules.BST_Node.Node(self.max_index, member))
            # insert into data storage struct

            self.insert_into_indexed_columns(member, self.max_index)
            # insert into BSTs for sorting and indexing

            self.max_index += 1

        else:  # if the list supplied doesn't fit the table attributes
            raise modules.exceptions.InvalidArgumentNumber("Table.insert()", len(attributes), len(self.attributes))

    def insert_into_indexed_columns(self, member, max_index):
        i = 0
        for attribute in self.attributes_keys:
            self.indexed_members[attribute].insert(modules.BST_Node.Node(member[i], max_index))
            i += 1

    def delete(self, key, attribute=None):
        if attribute == None:
            member = self.members.delete(key)
            # print(member)
            if member:
                i = 0
                for attribute in self.attributes_keys:
                    self.indexed_members[attribute].delete(member.other_data[i])
                    i += 1
        else:
            attribute_bst = self.indexed_members.get(attribute, None)
            if attribute_bst:
                abk = attribute_bst[key]
                for i in range(len(abk)):
                    index = abk[i].other_data
                    self.delete(index)

    def print_indexed_columns(self):
        for attribute in self.attributes_keys:
            print("{}: ".format(attribute))

            ordered_bst = []
            modules.DD_BST.list_infix(self.indexed_members[attribute].root, ordered_bst)

            print(ordered_bst, end="\n")

    def rebuild_all_indexes(self):
        nodes_infix = []
        nodes_infix = modules.DD_BST.list_infix(self.members.root, nodes_infix)
        self.members.rebuild_index(nodes_infix)

        i = 0
        for attribute in self.attributes_keys:
            self.indexed_members[attribute].root = None
            for j in range(len(nodes_infix)):
                self.indexed_members[attribute].insert(modules.BST_Node.Node(nodes_infix[j].other_data[i], j))
            self.indexed_members[attribute].balance()
            i += 1

def query(query_str):
        selected_table, selection = modules.queries.query(query_str)
        print("table: {}, selection: {}".format(selected_table,selection))

        result = ""

        table = table_list.get(selected_table, None)
        
        if table:
            nodes_infix = []
            try:
                if selection == "*":
                    nodes_infix = modules.DD_BST.list_infix(table.members.root, nodes_infix)
                else:
                    nodes_infix = modules.DD_BST.list_infix(table.indexed_members[selection].root, nodes_infix)
            except:
                result += "attribute '{}' doesn't exist".format(selection)
        else:
            return "table '{}' doesn't exist".format(selected_table)

        # print(nodes_infix)

        for node in nodes_infix:
            if selection == "*":
                result += f"{node.sorting_data} "
                for attribute in node.other_data:
                    result += f"| {attribute}"
            else:
                result += f"{node.other_data} | {node.sorting_data}"
            result += "\n"

        return result


def launch_demo():
    personne = create_table("personne", Table(p_number=[str, 10, "primary_key"], f_name=[str, 50], l_name=[str, 50]))

    personne.insert("0139474225", "Dimitri", "VINET")
    personne.insert("0239474225", "Fimitri", "AINET")
    personne.insert("0339474225", "Aimitri", "BINET")
    personne.insert("0439474225", "Kimitri", "WINET")
    personne.insert("0539474225", "Gimitri", "XINET")
    personne.insert("0639474225", "Gimitri", "HINET")

    print("\nList of members:")
    print(personne.members)
    print("\n===========================================================\n")
    time.sleep(1)

    print("Indexes:")
    print(personne.members[1])
    print(personne.members[7])
    print("\n===========================================================\n")
    time.sleep(1)

    print("Index rebuilding:")
    print("Deleting members...")
    personne.delete("Gimitri", "f_name")
    personne.delete(2)
    print('"Wrong" index: ')
    print(personne.members)
    personne.rebuild_all_indexes()
    print('"Good" index: ')
    print(personne.members)
    print("\n===========================================================\n")
    time.sleep(1)

    print("Queries:")
    print(query("FROM personne select *"))
    print(query("from personne select l_name"))
    print(query("from personne select z_name"))


                
launch_demo()

"""
personne = create_table("personne", Table(p_number=[str, 10, "primary_key"], f_name=[str, 50], l_name=[str, 50]))
personne.insert("0139474225", "Dimitri", "VINET")
personne.insert("0239474225", "Fimitri", "AINET")
personne.insert("0339474225", "Aimitri", "BINET")
personne.insert("0439474225", "Kimitri", "WINET")
personne.insert("0539474225", "Gimitri", "XINET")
personne.insert("0639474225", "Gimitri", "HINET")

print(personne.members)
print("================")
personne.print_indexed_columns()
print("================")
personne.delete("Gimitri", "f_name")
personne.delete(2)
personne.rebuild_all_indexes()
print(personne.members)
personne.print_indexed_columns()
print("================")
personne.indexed_members["f_name"].balance()
print(personne.indexed_members["f_name"]["Gimitri"])
print("================")
print(query("from personne select l_name"))



ordinateur = Table(serial_number=(str, 12, "primary_key"), OS=(str, 20), CPU=(str, 15), prix=(int, 10))
ordinateur.insert("892034983423", "Ubuntu 20.04", "Intel Core i5", 700)
 """