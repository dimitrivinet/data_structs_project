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

- select with table name and \*: with MySQL as an example, a SELECT with the \* argument returns all the columns of the table.

- select with a column name: returns all the values in the specified column, in alphabetical order, with the associated index next to the values.

- select with a wrong column name: returns an error message. Also works for table names.


## Code structure and explanation:

#### modules Package:

I use modules to clean up the main script file. The module names are hopefully self-explanatory but I will explain them with a bit more detail:

- **BST_Node**: Contains the class for the node of a BST. I separated it from the BST file for reusability.

- **DD_BST**: DD_BST means Double Data BST. I named it "Double Data" because it has "sorting data" (the value by which the BST is sorted, a.k.a. the variables) and "other data" (the index). It contains the structure for a BST, basic functions and other useful methods for balancing and listing the tree.

- **exceptions**: A custom exceptions module. I tried to make the code as foolproof as possible, but I still tried to make some useful exceptions for my database.

- **queries**: A module for interpreting queries. It decodes the user-provided query string and returns values to be used by the database system.

### Main python scripts:

- **phonebook.py**: phonebook.py is my first draft for a database. It fulfills all the requirements for the first level of the project, but doesn't use the same structure as the generic database. I only used a list for the data structure and the members have fixed types and lengths. 
You can add members with the += operator and search by any attribute with search_cs().

- **generic_database.py**: this is the main python script for this project. The main class is the Table class, which represents a table in a classic database. When you create a Table, it is logged in the table_list variable for later use.

The main data structures for this database are Binary Search Trees. There are n+1 for each table, where n is the number of columns: 1 for storing all the data and one for each column. The column BSTs are called indexed_columns and are stored in a dictionary.

Within this table, one column can be declared as a primary key which can be used for joining tables (not implemented).

When inserting in a table, the attributes for each column are checked against the requirements decided during table creation. If all attributes are good, the member is inserted in the general BST and in the attribute BSTs. If one of them is wrong, the member is not inserted anywhere.

You can delete from a table by index or attribute with the delete() function. To delete by index, leave the "attribute" argument to None, and if you want to delete by attribute, specify its name. A member will always be deleted from all BSTs.

To print the main BST, simply print the members variable of the table. You can print all the other BSTs at once with the prin_indexed_columns() function.

To rebuild the index, use the rebuild_all_indexes() function.
Finally, to make a query, use the query() function with your query as an argument. The syntax is the same as MySQL.



