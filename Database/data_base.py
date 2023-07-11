import sqlite3

#Create Database
conn = sqlite3.connect('test.db')

#Use connection to database to execute commands
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_sample( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_name TEXT)")
    conn.commit()
    #Use this tuple to iterate
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    #Iterate through tuple and insert files that end in .txt
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_sample(col_name) VALUES (?)", (file,))
            print(file)
#Close connection when finished with execution
conn.close()