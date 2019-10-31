import csv
import pymysql

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

database.execute('''CREATE TABLE League (
    Rank     INT NOT NULL AUTO_INCREMENT,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC   INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE Reds (
    Rank      INT NOT NULL,
    Name      VARCHAR(20) NOT NULL,
    Position  VARCHAR(14) NOT NULL,
    G         INT NOT NULL,
    PA        INT NOT NULL,
    HR        INT NOT NULL,
    R         INT NOT NULL,
    RBI       INT NOT NULL,
    SB        INT NOT NULL,
    BB       DECIMAL(5,3) NOT NULL,
    K        DECIMAL(5,3) NOT NULL,
    AVG       DECIMAL(5,3) NOT NULL,
    OBP       DECIMAL(5,3) NOT NULL,
    SLG       DECIMAL(5,3) NOT NULL,
    wOBA      DECIMAL(5,3) NOT NULL,
    wRC     INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE Catchers (
    Rank     INT NOT NULL,
    Name     VARCHAR(20) NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE FirstBasemen (
    Rank     INT NOT NULL,
    Name     VARCHAR(20) NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE SecondBasemen (
    Rank     INT NOT NULL,
    Name     VARCHAR(20) NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE ThirdBasemen (
    Rank     INT NOT NULL,
    Name     VARCHAR(20) NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE Shortstops (
    Rank     INT NOT NULL,
    Name     VARCHAR(20) NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

database.execute('''CREATE TABLE Outfielders (
    Rank     INT NOT NULL,
    Name     VARCHAR(20) NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB      DECIMAL(5,3) NOT NULL,
    K       DECIMAL(5,3) NOT NULL,
    AVG      DECIMAL(5,3) NOT NULL,
    OBP      DECIMAL(5,3) NOT NULL,
    SLG      DECIMAL(5,3) NOT NULL,
    wOBA     DECIMAL(5,3) NOT NULL,
    wRC    INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

file_League = open("League.csv", "r")
file_Reds = open("Reds.csv", "r")
file_Catchers = open("Catchers.csv", "r")
file_FirstBasemen = open("FirstBasemen.csv", "r")
file_SecondBasemen = open("SecondBasemen.csv", "r")
file_ThirdBasemen = open("ThirdBasemen.csv", "r")
file_Shortstops = open("Shortstops.csv", "r")
file_Outfielders = open("Outfielders.csv", "r")

leagueData = csv.reader(file_League, delimiter=',')
redsData = file_Reds.readlines()
catchersData = file_Catchers.readlines()
firstBasemenData = file_FirstBasemen.readlines()
secondBasemenData = file_SecondBasemen.readlines()
thirdBasemenData = file_ThirdBasemen.readlines()
shortstopsBasemenData = file_Shortstops.readlines()
outfieldersData = file_Outfielders.readlines()


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


database.close();
connect.commit();
connect.close();


