
from modules.BST import *
from modules.exceptions import *
from collections import OrderedDict
import numpy as np


class Table:
    def __init__(self, **attributes): #table is ordered dict with {attribute name: tuple of attribute characteristics (type, max length, isPrimaryKey)}
        self.attributes = OrderedDict()
        self.max_index = 0
        self.primary_key = ""

        for key, value in attributes.items():
            self.attributes[key] = value
            try:
                self.primary_key = value(3)
            except:
                pass

        self.attributes_keys = list(self.attributes.keys())
        # print(self.attributes_keys)
        self.members = BST()

    def insert(self, *attributes):
        if len(attributes) == len(self.attributes): #if the list supplied is the correct length

            for i in range(len(self.attributes)): #for each attribute of the table

                if type(attributes[i]) is self.attributes[self.attributes_keys[i]][0]: #check if type is correct

                    if type(attributes[i]) is str: #if the attribute is a string, check if the length is correct
                        if len(attributes[i]) <= self.attributes[self.attributes_keys[i]][1]:
                            pass
                    elif type(attributes[i]) is int: #if the attribute is an int, check if value is under max value (when only length is supplied in attribute definition)
                        if attributes[i] <= 10**(self.attributes[self.attributes_keys[i]][1] + 1):
                            pass

                    else:
                        raise InvalidAttributeLength(attributes[i], len(attributes[i]))

                else: #if attribute type is incorrect
                    raise InvalidAttributeType(attributes[i], type(attributes[i]))

            member = np.array(attributes)
            # print(member)

            self.members.insert(Node(self.max_index, member))
            self.max_index += 1

        else: #if the list supplied doesn't fit the table attributes
            raise InvalidArgumentNumber("Table.insert()", len(attributes), len(self.attributes))


class SELECT:
    def __init__(self, table, *attributes): #select takes attributes and a table and returns all values of only attributes for table
        pass


class JOIN:
    def __init__(self, table1, table2, attr1=None, attr2=None): #join takes 2 tables and optionnaly 2 attributes to join with
        pass


personne = Table(p_number=(str, 10, "primary_key"), f_name=(str, 50), l_name=(str, 50))
personne.insert("0139474225", "Dimitri", "VINET")
print(personne.members[0].data)

ordinateur = Table(serial_number=(str, 12, "primary_key"), OS=(str, 20), CPU=(str, 15), prix=(int, 10))
ordinateur.insert("892034983423", "Ubuntu 20.04", "Intel Core i5", 700)
