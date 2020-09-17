from modules import exceptions


class Phonebook:
    def __init__(self):
        self.data_struct = []

    def __str__(self):
        str_out = ""
        for i in range(len(self.data_struct)):
            str_out += "{0}; ".format(self.data_struct[i])
        return str_out

    def __iadd__(self, other):
        self.data_struct.append(other)
        return self

    def __add__(self,other):
        self.data_struct.append(other)

    def search_cs(self, query):
        result = []
        for elem in self.data_struct:
            if elem.number == query or elem.f_name == query or elem.l_name == query:
                result.append(elem)

        return result


class Person:
    def __init__(self, number, f_name, l_name):
        number_len = len(number)
        if number_len == 10:
            self.number = number
        else:
            raise exceptions.InvalidAttributeLength("number", number_len)

        f_name_len = len(f_name)
        if f_name_len < 50:
            self.f_name = f_name
        else:
            raise exceptions.InvalidAttributeLength("f_name", f_name_len)

        l_name_len = len(l_name)
        if l_name_len < 50:
            self.l_name = l_name
        else:
            raise exceptions.InvalidAttributeLength("l_name", l_name_len)

    def __str__(self):
        return '{0}, {1} {2}'.format(self.number, self.f_name, self.l_name)


# Create phonebook:
phonebook1 = Phonebook()

# Create People: 
alex = Person("01234567891", "Alex", "Dru")
thomas = Person("2345678901", "Thomas", "Juldo")

# Add people to phonebook:
phonebook1 += alex
phonebook1 += thomas

# Print phonebook
print(phonebook1)

# Look up people with any attribute and print results:
result = phonebook1.search_cs("0123456789")
for item in result:
    print(item)

