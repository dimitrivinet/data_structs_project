from modules import exceptions
import collections


class Table:
    def __init__(self, **attributes):
        self.attributes = collections.OrderedDict()
        self.primary_key = ""
        for key, value in attributes.items():
            self.attributes[key] = value
            try:
                self.primary_key = value(3)
            except:
                pass

    def insert(self, *attributes):
        if len(attributes) == len(self.attributes):
            #TODO: ajout d'un élément à une table
            pass
        else:
            raise exceptions.InvalidArgumentNumber("Table.insert()", len(attributes), len(self.attributes))


personne = Table(p_number = ("int", 10, "primary_key"), f_name = ("string", 50), l_name = ("string", 50))
personne.insert("0139474225", "Dimitri", "VINET")