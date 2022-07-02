import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Shang-Chi and the Legend of the Ten Rings','Simu Liu','Awkwafina','Destin Daniel Cretton',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Dune','Timothée Chalamet','Rebecca Ferguson','Denis Villeneuve',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('bigil: Homecoming',Vijay','Thara','Atlee',2020)")
pointer.execute("INSERT INTO MOVIES VALUES('Spider-Man: Far From Home','Tom Holland','Zendaya','Jon Watts',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('Avengers','Mansoor Ali Khan','Rashmika','mothi',2023)")

allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

print("*********Actor Query*********")
name=input("enter the actor name: ")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = '"+name+"'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")