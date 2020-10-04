class InvalidAttributeLength(Exception):
    def __init__(self, elem = None, len = None):
        self.message = "Attribute {0} has invalid length {1}".format(elem, len)
        super().__init__(self.message)

class InvalidArgumentNumber(Exception):
    def __init__(self, func = None, received = None, expected = None):
        self.message = "Function {0} received {1} arguments, expected {2}".format(func, received, expected)
        super().__init__(self.message)

class InvalidAttributeType(Exception):
    def __init__(self, elem = None, type = None):
        self.message = "Attribute {0} has invalid type {1}".format(elem, type)
        super().__init__(self.message)