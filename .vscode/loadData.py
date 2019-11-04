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
    LeagueRankId     INT NOT NULL,
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
    PRIMARY KEY (LeagueRankId)
)''');

database.execute('''CREATE TABLE Reds (
    RankId      INT NOT NULL,
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    Age       INT NOT NULL,
    Height    VARCHAR(6),
    Weight    VARCHAR(7),
    Country VARCHAR(25),
    Position  VARCHAR(14) NOT NULL,
    PRIMARY KEY (RankId)
)''');

database.execute('''CREATE TABLE Catchers (
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    TeamRank      INT NOT NULL,
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
    PRIMARY KEY (FirstName, LastName),
    FOREIGN KEY (TeamRank) REFERENCES Reds(RankId)
)''');

database.execute('''CREATE TABLE FirstBasemen (
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    TeamRank      INT NOT NULL,
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
    PRIMARY KEY (FirstName, LastName),
    FOREIGN KEY (TeamRank) REFERENCES Reds(RankId)
)''');

database.execute('''CREATE TABLE SecondBasemen (
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    TeamRank      INT NOT NULL,
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
    PRIMARY KEY (FirstName, LastName),
    FOREIGN KEY (TeamRank) REFERENCES Reds(RankId)
)''');

database.execute('''CREATE TABLE ThirdBasemen (
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    TeamRank      INT NOT NULL,
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
    PRIMARY KEY (FirstName, LastName),
    FOREIGN KEY (TeamRank) REFERENCES Reds(RankId)
)''');

database.execute('''CREATE TABLE Shortstops (
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    TeamRank      INT NOT NULL,
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
    PRIMARY KEY (FirstName, LastName),
    FOREIGN KEY (TeamRank) REFERENCES Reds(RankId)
)''');

database.execute('''CREATE TABLE Outfielders (
    FirstName      VARCHAR(20) NOT NULL,
    LastName      VARCHAR(20) NOT NULL,
    TeamRank      INT NOT NULL,
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
    PRIMARY KEY (FirstName, LastName),
    FOREIGN KEY (TeamRank) REFERENCES Reds(RankId)
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
    rank = lines[0]
    team = lines[1]
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

    sql = "INSERT INTO League (LeagueRankId, Team, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (rank, team, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

    database.execute(sql, vals)

#load data for reds table
for lines in redsData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
   position = lines[3]
   age = lines[4]
   height = lines[5]
   weight = lines[6]
   country = lines[7]

   sql = "INSERT INTO Reds (RankId, FirstName, LastName, Age, Height, Weight, Country, Position) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (rank, firstName, lastName, age, height, weight, country, position)

   database.execute(sql, vals)

#load data for catchers table
for lines in catchersData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
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

   sql = "INSERT INTO Catchers (FirstName, LastName, TeamRank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, rank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for firstbasemen table
for lines in firstBasemenData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
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

   sql = "INSERT INTO FirstBasemen (FirstName, LastName, TeamRank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, rank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for secondbasemen table
for lines in secondBasemenData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
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

   sql = "INSERT INTO SecondBasemen (FirstName, LastName, TeamRank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, rank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for thirdbasemen table
for lines in thirdBasemenData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
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

   sql = "INSERT INTO ThirdBasemen (FirstName, LastName, TeamRank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, rank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for shortstops table
for lines in shortstopsBasemenData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
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

   sql = "INSERT INTO Shortstops (FirstName, LastName, TeamRank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, rank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)

#load data for outfielders table
for lines in outfieldersData:
   rank = lines[0]
   firstName = lines[1]
   lastName = lines[2]
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

   sql = "INSERT INTO Outfielders (FirstName, LastName, TeamRank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
   vals = (firstName, lastName, rank, G, PA, HR, R, RBI, SB, BB, K, AVG, OBP, SLG, wOBA, wRC)

   database.execute(sql, vals)



database.close(); 
connect.commit(); 
connect.close(); #close connection

#end loading


