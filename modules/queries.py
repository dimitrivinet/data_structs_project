
class InvalidQuery(Exception):
    def __init__(self, error):
        self.message = "Exception: invalid query (error in {})".format(error)
        super().__init__(self.message)


def query(query_str):
    selection = ""
    table = ""
    split_query = query_str.split(" ")
    # print(split_query)

    try:
        if split_query[0] == 'from':
            table = split_query[1]
        else:
            raise InvalidQuery("from")

        if split_query[2] == 'select':
            selection = split_query[3]
        else:
            raise InvalidQuery("select")

        return table, selection
    except:
        raise InvalidQuery("query format")


# query("select p_number from personne")
