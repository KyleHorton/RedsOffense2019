import csv
import pymysql

# Author:Kyle Horton
# Project: RedsOffenseDB + Visualization

#establish sql connection
def make_connection():
    return pymysql.connect(
        host='reds-offense.c63ijpxfdwey.us-east-1.rds.amazonaws.com',
        user='admin', 
        password='baseball',
        port=3306,
        autocommit=True)

connect = make_connection()
database = connect.cursor()

# setting up DB Schema

database.execute('DROP DATABASE IF EXISTS RedsOffense');
database.execute('CREATE DATABASE RedsOffense');
database.execute('USE RedsOffense');

database.execute('DROP TABLE IF EXISTS League');
database.execute('DROP TABLE IF EXISTS Reds');
database.execute('DROP TABLE IF EXISTS Catchers');
database.execute('DROP TABLE IF EXISTS FirstBasemen');
database.execute('DROP TABLE IF EXISTS SecondBasemen');
database.execute('DROP TABLE IF EXISTS ThirdBasemen');
database.execute('DROP TABLE IF EXISTS Shortstops');
database.execute('DROP TABLE IF EXISTS Outfielders');

#creating schemas for each table
database.execute('''CREATE TABLE League (
    RankId     INT NOT NULL AUTO_INCREMENT,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC   INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE Reds (
    RankId      INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    Position  VARCHAR(14) NOT NULL,
    G         INT NOT NULL,
    PA        INT NOT NULL,
    HR        INT NOT NULL,
    R         INT NOT NULL,
    RBI       INT NOT NULL,
    SB        INT NOT NULL,
    BB       VARCHAR(5) NOT NULL,
    K        VARCHAR(5) NOT NULL,
    AVG       DECIMAL(5,3) NOT NULL,
    OBP       DECIMAL(5,3) NOT NULL,
    SLG       DECIMAL(5,3) NOT NULL,
    wOBA      DECIMAL(5,3) NOT NULL,
    wRC     INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE Catchers (
    RankId     INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE FirstBasemen (
    RankId     INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE SecondBasemen (
    RankId     INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE ThirdBasemen (
    RankId     INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE Shortstops (
    RankId     INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE Outfielders (
    RankId     INT NOT NULL AUTO_INCREMENT,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      VARCHAR(5) NOT NULL,
    K       VARCHAR(5) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (RankId)
)''');

#opening each data file
file_League = open("../League.csv", "r")
file_Reds = open("../Reds.csv", "r")
file_Catchers = open("../Catchers.csv", "r")
file_FirstBasemen = open("../FirstBasemen.csv", "r")
file_SecondBasemen = open("../SecondBasemen.csv", "r")
file_ThirdBasemen = open("../ThirdBasemen.csv", "r")
file_Shortstops = open("../Shortstops.csv", "r")
file_Outfielders = open("../Outfielders.csv", "r")

#reading each data file
leagueData = csv.reader(file_League, delimiter=',')
redsData = csv.reader(file_Reds, delimiter=',')
catchersData = csv.reader(file_Catchers, delimiter=',')
firstBasemenData = csv.reader(file_FirstBasemen, delimiter=',')
secondBasemenData = csv.reader(file_SecondBasemen, delimiter=',')
thirdBasemenData = csv.reader(file_ThirdBasemen, delimiter=',')
shortstopsBasemenData = csv.reader(file_Shortstops, delimiter=',')
outfieldersData = csv.reader(file_Outfielders, delimiter=',')

#load data for league table
for lines in leagueData:
    team = lines[0]
    G = lines[1]
    PA = lines[2]
    HR = lines[3]
    R = lines[4]
    RBI = lines[5]
    SB = lines[6]
    BB = lines[7]
    K = lines[8]
    AVG = lines[9]
    OBP = lines[10]
    SLG = lines[11]
    wOBA = lines[12]
    wRC = lines[13]

    sql = "INSERT INTO League (Team, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (team, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

    database.execute(sql, vals)

#load data for reds table
for lines in redsData:
   firstName = lines[0]
   lastName = lines[1]
   position = lines[2]
   G = lines[3]
   PA = lines[4]
   HR = lines[5]
   R = lines[6]
   RBI = lines[7]
   SB = lines[8]
   BB = lines[9]
   K = lines[10]
   AVG = lines[11]
   OBP = lines[12]
   SLG = lines[13]
   wOBA = lines[14]
   wRC = lines[15]

   sql = "INSERT INTO Reds (FirstName, LastName, Position, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, position, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for catchers table
for lines in catchersData:
   firstName = lines[0]
   lastName = lines[1]
   G = lines[2]
   PA = lines[3]
   HR = lines[4]
   R = lines[5]
   RBI = lines[6]
   SB = lines[7]
   BB = lines[8]
   K = lines[9]
   AVG = lines[10]
   OBP = lines[11]
   SLG = lines[12]
   wOBA = lines[13]
   wRC = lines[14]

   sql = "INSERT INTO Catchers (FirstName, LastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for firstbasemen table
for lines in firstBasemenData:
   firstName = lines[0]
   lastName = lines[1]
   G = lines[2]
   PA = lines[3]
   HR = lines[4]
   R = lines[5]
   RBI = lines[6]
   SB = lines[7]
   BB = lines[8]
   K = lines[9]
   AVG = lines[10]
   OBP = lines[11]
   SLG = lines[12]
   wOBA = lines[13]
   wRC = lines[14]

   sql = "INSERT INTO FirstBasemen (FirstName, LastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for secondbasemen table
for lines in secondBasemenData:
   firstName = lines[0]
   lastName = lines[1]
   G = lines[2]
   PA = lines[3]
   HR = lines[4]
   R = lines[5]
   RBI = lines[6]
   SB = lines[7]
   BB = lines[8]
   K = lines[9]
   AVG = lines[10]
   OBP = lines[11]
   SLG = lines[12]
   wOBA = lines[13]
   wRC = lines[14]

   sql = "INSERT INTO SecondBasemen (FirstName, LastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for thirdbasemen table
for lines in thirdBasemenData:
   firstName = lines[0]
   lastName = lines[1]
   G = lines[2]
   PA = lines[3]
   HR = lines[4]
   R = lines[5]
   RBI = lines[6]
   SB = lines[7]
   BB = lines[8]
   K = lines[9]
   AVG = lines[10]
   OBP = lines[11]
   SLG = lines[12]
   wOBA = lines[13]
   wRC = lines[14]

   sql = "INSERT INTO ThirdBasemen (FirstName, LastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for shortstops table
for lines in shortstopsBasemenData:
   firstName = lines[0]
   lastName = lines[1]
   G = lines[2]
   PA = lines[3]
   HR = lines[4]
   R = lines[5]
   RBI = lines[6]
   SB = lines[7]
   BB = lines[8]
   K = lines[9]
   AVG = lines[10]
   OBP = lines[11]
   SLG = lines[12]
   wOBA = lines[13]
   wRC = lines[14]

   sql = "INSERT INTO Shortstops (FirstName, LastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for outfielders table
for lines in outfieldersData:
   firstName = lines[0]
   lastName = lines[1]
   G = lines[2]
   PA = lines[3]
   HR = lines[4]
   R = lines[5]
   RBI = lines[6]
   SB = lines[7]
   BB = lines[8]
   K = lines[9]
   AVG = lines[10]
   OBP = lines[11]
   SLG = lines[12]
   wOBA = lines[13]
   wRC = lines[14]

   sql = "INSERT INTO Outfielders (FirstName, LastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)



database.close();
connect.commit();
connect.close();

#end loading


