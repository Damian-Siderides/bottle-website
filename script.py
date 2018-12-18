# import sqlite3
# conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
# conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
# conn.commit()


"""

database fields

id, username, password, 

another table for various question statistics
maybe a table for each statistic?


number correct, number incorrect, total attempts, 



website features: login, register
salted passwords


"""



import sqlite3
conn = sqlite3.connect('data.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE data (id INTEGER PRIMARY KEY, username char NOT NULL, password NOT NULL)")
conn.execute("INSERT INTO data (username, password) VALUES ('boss', '')")
conn.execute("INSERT INTO data (username, password) VALUES ('admin', 'pass')")
conn.execute("INSERT INTO data (username, password) VALUES ('damian', 'word')")
conn.execute("INSERT INTO data (username, password) VALUES ('john', 'kek')")
conn.commit()