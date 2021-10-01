import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="nandita@123",database="my movies")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE film_List(Name VARCHAR(30),Actor VARCHAR(30),Actress VARCHAR(30),Director VARCHAR(30),Year_of_release INT NOT NULL,PRIMARY KEY(Name))")
sql = "INSERT INTO film_List (Name, Actor, Actress,Director,Year_of_release) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Forrest grump',' Robert Zemeckis','Tom Hanks','Robin Wright',1994),
  ('Parasite','Bong Joon-ho','Park Seo‑joon','Cho Yeo‑jeong',2019),
  ('Titanic',' James Cameron','Leonardo DiCaprio','Kate Winslet',1997),
  ('The Faults in Our Stars','Ansel Elgort','Shailene Woodley','Josh Boone',2014),
  ('La La Land','Damien Chazelle','Ryan Gosling','Emma Stone',2019),
  ('One Flew Over The Cuckoo's Nest',Milos forman','Jack nicholson','Louise Fletcher',1975),
  ('The truman show ','peter weir','Jim carrey','Laura Linney',1998),
  ('Pulp fiction','Quentin Tarantino',' Samuel L Jackson','Uma Thuram',1994)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Contents inserted.")
mycursor.execute(" SELECT * FROM film_List")
for i in mycursor:
    print(i)
mycursor.execute("SELECT Name,Actor FROM film_List ORDER BY Actor")
for j in mycursor:
    print(j)
mydb.close()