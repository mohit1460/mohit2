 #QUESTION1
import sqlite3
conn=sqlite3.connect("09999900.db")
print("opened database successsfuly")

conn.execute('''CREATE TABLE  Book
             (BOOKID    INT PRIMARY KEY      NOT NULL,
              TITLEID   INT                 NOT NULL,
           LOCATION    VARCHAR                 NOT NULL,
             GENRE       TEXT   )''')
print("table created successsfully")
conn.execute('''CREATE TABLE  Titles
            (TITLEID           INT PRIMARY KEY      NOT NULL,
             TITLE               TEXT           NOT NULL,
            ISBN                VARCHAR          NOT NULL,
            PUBlISHERID         INT,
            PUBLISHYEAR      INT  )''')
print("table created successsfully")
conn.execute('''CREATE TABLE  Publishers
             (PUBLISHERID      INT  PRIMARY KEY      NOT NULL,
             NAME               TEXT                  NOT NULL,
          STREETADDRESS     VARCHAR                  NOT NULL,
         SUITENUMBER        CHAR(50),
            ZIPCODEID          INT )''')
print("table created successsfully")

conn.execute('''CREATE TABLE  Zipcode
            (ZIPCODEID INT PRIMARY KEY      NOT NULL,
            CITY         TEXT           NOT NULL,
            STATE        TEXT           NOT NULL,
            ZIPCODE      INT )''')
print("table created successsfully")

conn.execute('''CREATE TABLE  Authorstitles
            (AUTHORTITLEID TEXT PRIMARY KEY      NOT NULL,
             AUTHORID        INT           NOT NULL,
             TITLEID         INT           NOT NULL)''')
print("table created successsfully")

conn.execute('''CREATE TABLE  Authors
             (AUTHORID     INT PRIMARY KEY      NOT NULL,
              FIRSTNAME    TEXT                NOT NULL,
              MIDDLENAME   TEXT           ,
             LASTNAME     TEXT                NOT NULL)''')
print("table created successsfully")

#QUESTION2

conn.execute("INSERT INTO Book(BOOKID,TITLEID,LOCATION,GENRE) VALUES(1,123,'California','FICTION')")
conn.execute("INSERT INTO Titles(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHYEAR) VALUES(136,'PAUL',32,4343,9999)")
conn.execute("INSERT INTO Publishers(PUBLISHERID,NAME,STREETADDRESS,SUITENUMBER,ZIPCODEID) VALUES(130,'MOHIT','STREET NO 32 California',246,1555)")
conn.execute("INSERT INTO Zipcode(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES(8,'NAHAN','HP',14333)")
conn.execute("INSERT INTO Authorstitles(AUTHORTITLEID,AUTHORID,TITLEID) VALUES(999,7887,32)")
conn.execute("INSERT INTO Authors(AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME) VALUES(199,'MOHIT',NULL,'SHARMA')")
conn.commit()
print("values inserted")

#QUESTION3

cursor= conn.execute("SELECT BOOKID,TITLEID,LOCATION,GENRE FROM Book")
for row in cursor:
    print("BOOKID= ",row[0])
    print("TITLEID",row[1])
    print("LOCATION",row[2])
    print("GENRE",row[3])
print("operation done successfully")

cursor1= conn.execute("SELECT TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHYEAR FROM Titles")
for row1 in cursor1:
    print("TITLEID",row1[0])
    print("TITLE",row1[1])
    print("ISBN",row1[2])
    print("PUBLISHERID",row1[3])
    print("PUBLISHYEAR",row1[4])
print("operation done successfully")

cursor2= conn.execute("SELECT PUBLISHERID,NAME,STREETADDRESS,SUITENUMBER,ZIPCODEID FROM Publishers")
for row2 in cursor2:
    print("PUBLISHERID= ",row2[0])
    print("NAME",row2[1])
    print("STREETADDRESS",row2[2])
    print("SUITENUMBER",row2[3])
    print("ZIPCODEID",row2[4])
print("operation done successfully")

cursor3= conn.execute("SELECT ZIPCODEID,CITY,STATE,ZIPCODE  FROM Zipcode")
for row3 in cursor3:
    print("ZIPCODEID ",row3[0])
    print("CITY",row3[1])
    print("STATE",row3[2])
    print("ZIPCODE",row3[3])
print("operation done successfully")


cursor4= conn.execute("SELECT AUTHORTITLEID,AUTHORID,TITLEID  FROM Authorstitles")
for row4 in cursor4:
    print("AUTHORTITLEID",row4[0])
    print("AUTHORID",row4[1])
    print("TITLEID",row4[2])
print("operation done successfully")

cursor5= conn.execute("SELECT AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME FROM Authors")
for row5 in cursor5:
    print("AUTHORID",row5[0])
    print("FIRSTNAME",row5[1])
    print("MIDDLENAME",row5[2])
    print("LASTNAME",row5[3])
print("operation done successfully")

#QUESTION3


conn.execute("UPDATE Book set TITLEID = 1111 where BOOKID =1")
cursor= conn.execute("SELECT BOOKID,TITLEID,LOCATION,GENRE FROM Book")
conn.commit()
for row in cursor:
    print("BOOKID",row[0])
    print("TITLEID",row[1])
    print("LOCATION",row[2])
    print("GENRE",row[3])
print("operation done successfully")

print("total number of rows updated",conn.total_changes)