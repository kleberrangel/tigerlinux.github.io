#!/usr/bin/env python
#
# By Reynaldo R. Martinez P.
# Sept 26, 2016
# TigerLinux AT Gmail DOT Com
# SAMPLE SQLITE ACCESS WITH SQLALCHEMY
# SQLAlchemy 1.0.x
#

print ("")

# NOTE: Ensure to have available SQLAlchemy libs:
# pip install sqlalchemy (generic python)
# pip3 install sqlalchemy (python 3)
# pip2 install sqlalchemy (python 2)
# Also, ensure you have installed sqlite

# We'll use sqlalchemy with simple sqlite database in order
# to show how to access a database and perform common SQL
# operations on it:

# First, we need to import sqlalchemy:

from sqlalchemy import *

# We need to create our database object. This is performed
# with the "create_engine" class.
# The URL must be in the form:
# sqlite:///filename

dbfilename = "catsdb.db"
dburl = "sqlite:///" + dbfilename

# Set the "False" to "True" in order to see all the DB operations
# in standard output !!
# database = create_engine(dburl, echo=True)
database = create_engine(dburl, echo=False)

# The last statement created our class istance, called "database", from the
# create_engine class. If you change echo=False to True, all DB operations
# will be echoed to standard output.

# The following statement is called in order to create the object that will
# manage all our database interactions

dbmetadata = MetaData(database)

# Then, dburl -> database -> dbmetadata

# Now, with the dbmetadata object ready, we can begin creating thins. We'll
# proceed to create a table. For that, we need to call the "Table" function
# from sqlalchemy

mycats = Table("cats", dbmetadata,
    Column("cat_id",Integer,Sequence('cat_id_seq'), primary_key=True),
    Column("cat_name",String(50)),
    Column("cat_color",String(50)),
    Column("cat_weight",Float),
    Column("mouse_face",Boolean)
)

# The last statements create the table definition inside the "dbmetadata" object,
# but it does not create the table (not yet). The table will be created by using
# the following statement:

mycats.create(database, checkfirst=True)

# In this point, the "catsdb.db" file is created in your home dir, and the table inside
# the database. Note the "checkfirst=True". This will check if the table is already there.
# If it's there, it will not re-create it. Case else, normal conditions apply and the
# table will be created

# Now, let's insert some data on the database by calling the following class:

myinsert = mycats.insert()

# And:

# First, with a single row:
myinsert.execute(
    cat_name="Kiki",
    cat_color="Base white with black spots",
    cat_weight=3.0,
    mouse_face=True
)

#Now, with more than one row:

myinsert.execute(
    {"cat_name": "Rayita", "cat_color": "Creamy white with grey-listed patches", "cat_weight": 3.5, "mouse_face": False},
    {"cat_name": "Negrito", "cat_color": "Base black with white patches and white belly", "cat_weight": 4.5, "mouse_face": False}
)

# After you inserted the data, destroy the object:

del myinsert

# Please always do a proper clean-up !. Don't keep objects referencing your tables, or
# you'll be unable to drop-them os properlly close access to the database objects !.

# With our data almost complete, we can do some selects. The same way we did with
# the "insert", we can do with the select:

myselect = mycats.select()
#and
selectexec = myselect.execute()

# Then, let's get some "cat" data... jejej:

myrow = selectexec.fetchone()

# The last statement got a row from our table "cats" and feed all data to the "myrow"
# as a "intelligent row object". See the following prints:

print ("")
print (type(myrow))
print (myrow)
print ("\nPrinting row objects:\n")
print ("ID: " + str(myrow[0]))
print ("\tCat Name: " + myrow["cat_name"])
print ("\tCat Color: " + myrow["cat_color"])
print ("\tCat Weight: " + str(myrow["cat_weight"]))
print ("\tMouse Face ??: " + str(myrow["mouse_face"]))

print ("")

# Destroy the objects, and call it again. Just for fun !.. jeje

del myrow,selectexec,myselect

myselect = mycats.select()
selectexec = myselect.execute()

# Now, let's see trough all the data:
# See that we can access the row-data by more
# than one way:

for row in selectexec:
    print ("ID: " + str(row.cat_id))
    print ("\tCat Name: " + row.cat_name)
    print ("\tCar Color: " + row[mycats.c.cat_color])
    print ("\tCar Weight: " + str(row.cat_weight))
    print ("\tMouse Face ??: " + str(row["mouse_face"]))

# Again, delete the objects to free the database access. No locks here !!

del selectexec,myselect

# We can reference queries in more specific ways. For easy of use, let's
# define a function that we'll use to run our queries:

def runmyquery(myquery):
    print ("\nQuery Begin\n")
    runselect = myquery.execute()
    for myrow in runselect:
        print ("Row: " + str(myrow))
    # Free the objects after use:
    del runselect,myquery
    print ("\nQuery End\n")

# And, the let's play

# All cat's which name is "kiki". This will return only one row.
query = mycats.select(mycats.c.cat_name == "Kiki")
runmyquery(query)

# All cat's without a mouse face... two rows, one for "Rayita", and one 
# for "Negrito"
query = mycats.select(mycats.c.mouse_face == False)
runmyquery(query)

# All cat's that weights less than 4.0 AND whose names are not Rayita. This will
# return only "Kiki"
query = mycats.select(and_(mycats.c.cat_weight < 4.0, mycats.c.cat_name != "Rayita"))
runmyquery(query)

# All cat's with a "a" in the name. Only "Rayita" will be returned:
query = mycats.select(mycats.c.cat_name.like("%a%"))
runmyquery(query)

# All cat's whose name start's with "N". Only "Negrito" will be returned:
query = mycats.select(mycats.c.cat_name.startswith("N"))
runmyquery(query)

# Note that our function "runmyquery" do a proper clean up on any created
# onbject, including the query, in order to avoid any further lock up of
# the referenced tables.

# Now, let's play with joins !. This time, we'll create another table which
# will reference our main table with a foreign-key:

mycatsbehaviour = Table("catsbehaviour", dbmetadata,
    Column("id",Integer,Sequence('id_seq'), primary_key=True),
    Column("cat_specifics",String(50)),
    Column("cat_spirit",String(50)),
    Column("cat_id", Integer, ForeignKey('cats.cat_id'))
)

# Again, try to drop it if it exists
mycatsbehaviour.drop(database, checkfirst=True)
mycatsbehaviour.create(database, checkfirst=True)

# And, let's include some data:

myinsert2 = mycatsbehaviour.insert()

myinsert2.execute(
    {"cat_specifics": "Crazy, but kindred", "cat_spirit": "Angel with mouse face!!", "cat_id": 1},
    {"cat_specifics": "Normally well mooded", "cat_spirit": "Angel with claws!!", "cat_id": 2},
    {"cat_specifics": "Well mooded only within he's relatives", "cat_spirit": "A Cat-Lord in all situations", "cat_id": 3}
)

# Clean up:
del myinsert2

# Now, Joined Queries:
# This will return the data for both tables, where the cat_id's are the same:
query=select([mycats,mycatsbehaviour],mycats.c.cat_id == mycatsbehaviour.c.cat_id)
runmyquery(query)

# You can just print some data from the tables:
query=select([mycats.c.cat_name,mycatsbehaviour.c.cat_spirit],mycats.c.cat_id == mycatsbehaviour.c.cat_id)
runmyquery(query)

# Also, sqlalchemy support join function directly for a more smart way of joining:
query = join(mycats,mycatsbehaviour).select()
runmyquery(query)

# Now, let's do some changes. Let's insert another two rows in our tables:

insert1 = mycats.insert()
insert2 = mycatsbehaviour.insert()

insert1.execute(
    cat_name="Kisa",
    cat_color="Lynx grey-white wild pattern",
    cat_weight=10.0,
    mouse_face=False
)

insert2.execute(
    cat_specifics="Lynx mood... with a lot of claw-usage",
    cat_spirit="Another Angel... when she is in good mood.. ejjeje",
    cat_id=4
)

# Clean up... please !!
del insert1,insert2

# And, run our join again:
query=select([mycats,mycatsbehaviour],mycats.c.cat_id == mycatsbehaviour.c.cat_id)
runmyquery(query)

# Let's make an update.. We'll change Id=4 name (Kisa) by "Lynzon Kison":

# First, let's define an update object:
update1 = mycats.update().\
    where(mycats.c.cat_name == "Kisa").\
    values(cat_name = "Lynzon Kison")

# Then, execute the update
update1.execute()

# And, let's see the result:
query = mycats.select(mycats.c.cat_name.startswith("L"))
runmyquery(query)

# Clean up... again:
del update1


# The following drop will fail if you have any open object locking the
# database. BEWARE !!!. Delete all objects referencing insert's or selects
# before droping your database
mycatsbehaviour.drop(database, checkfirst=True)
mycats.drop(database, checkfirst=True)
# Note something very important here. In SQLite you'll don't see any error, but,
# if you are using mysql/mariadb, and try to delete mycats first, you'll end with
# a constraint violation as "mycatsbehaviour" database uses "cat_id" from "mycats"
# as a foreing key.

# As a final clean up, delete the MetaData and engine objects:

del dbmetadata,database

print ("")
# END
