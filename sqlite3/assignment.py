import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# open connection to database
conn = sqlite3.connect("assignment.db")

# while connection is open execute the following code
with conn:
    cur = conn.cursor()
    # create our table if it doesn't exist
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")

    # iterate through fileList and insert and print files that end with '.txt' 
    for i in fileList:
        if i.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (i,))
            print(i)
