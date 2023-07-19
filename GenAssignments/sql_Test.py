import sqlite3

#--------Assignment 1-4--------
# connection = sqlite3.connect("C:\Users\jbike\LocalMyDocs\DevProjects\Python_Projects\GenAssignments\databases")
# c = connection.cursor()
# c.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT")
# c.execute("INSERT INTO People VALUES('Ron', 'Obvious ' , 42)")
# connection.commit()
# connection = sqlite3.connect(':memory:')
# c.execute("DROP TABLE IF EXISTS People")
# connection.close()
# with sqlite3.connect("test database .db") as connection:
#     pass
#     #perform any SQL operations using connection here

# with sqlite3.connect('test database.db') as connection:
#     c = connection.cursor()
#     c.executescript ("""DROP TABLE IF EXISTS People;
#     CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT);
#     INSERT INTO People VALUES( 'Ron', 'Obvious' ,'42');
#     """)

# peopleValues = (('Luigi', 'Vercotti' , 43),('Arthur', 'Belling', 28))
# c.executemany("INSERT INTO People VALUES (?,?,?)", peopleValues)


#--------Assignment 5--------
# #get personal data from user and insert into a tuple
# firstName = input("Enter your first name.")
# lastName = input("Enter your last name.")
# age = int (input("Enter your age."))
# personData = (firstName, lastName, age)

# # execute insert statement for supplied person data
# with sqlite3.connect('testdatabase.db') as connection:
#     c = connection.cursor()
#     line = "INSERT INTO People VALUES('"+ firstName +"', '"+ lastName +"',"+ str(age) +")"
#     c.execute(line)


#--------Assignment 6--------
# #execute insert statement for supplied person data
# with sqlite3.connect('test database.db') as connection:
#     c = connection.cursor()
#     c.execute("INSERT INTO People VALUES (?,?, ?)", personData)

# c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
#     (45,'Luigi','Vercotti '))


# #--------Assignment 7--------
# peopleValues = (('Ron', 'Obvious', 42),('Luigi','Vercotti', 43),('Arthur' ,'Belling', 28))

# with sqlite3.connect('testdatabase.db') as connection:
#     c = connection.cursor()
#     c.execute("DROP TABLE IF EXISTS People")
#     c.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT)")
#     c.executemany ("INSERT INTO People VALUES (?,?,?)", peopleValues)

#     # select all first and last names from people over age 30
#     c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
#     for row in c.fetchall() :
#         print(row)


#--------Assignment 8--------
c.execute("SELECT FirstName,LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
