import sqlite3

conn = sqlite3.connect('C:\\Users\\jbike\\OneDrive\\Desktop\\PythonTests\\Challenges\\dbs.db')

peopleValues = (('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100),("Ak'not", "Mangalore", -5))

with conn:
    c = conn.cursor()
    c.execute("CREATE TABLE People (Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
    c.execute("UPDATE People SET Species=? WHERE Name=?", ("Human", "Korben Dallas"))
    conn.commit()
    c.execute("SELECT Name, IQ FROM People WHERE Species = Human")
    for row in c.fetchall() :
        print(row)
conn.close()