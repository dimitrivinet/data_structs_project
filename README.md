# data_structs_project

Dimitri VINET's Data Structures and Algorithms Project Repository.

## Demo breakdown:

Launch demo with ``` python3 generic_database.py ```

Each section of the demo represents an instruction as given by the table in the project description pdf.

##### Section 1: List of members

This section shows the contents of the database, which has a general structure: it supports any number of columns, and the user can choose which type the columns contain, as well as the maximum length of the attributes and if they are a primary key or not.


##### Section 2: Indexes

This section shows the use of indexes in looking up data within the database. The results shown come from a search with only an index; an index of 1 returns a member of the "personne" table, and an index of 7 returns None, because the database doesn't have a member with an index of 7.

##### Section 3: Index rebuilding

This section shows the rebuilding of indexes and its usefulness. After deleting members (possible with both an attribute value and an index), we show the "wrong" index: there are holes in the index. However, when we rebuild the index, the holes disappear and we can show the "right" index. This also works when we add another member which is sorted in the middle of the other members.


##### Section 4: Queries

This section shows my implementation of queries. It only goes up to a normal FROM *table* SELECT *column*, but you can write the query as if you were in MySQL for example.

There are three cases shown for this section:

- select with table name and "\*": with MySQL as an example, a SELECT with the "\*" argument returns all the columns of the table.

- select with a column name: returns all the values in the specified column, in alphabetical order, with the associated index next to the values.

- select with a wrong column name: returns an error message. Also works for table names.




