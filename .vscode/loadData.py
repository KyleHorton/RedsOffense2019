import csv
import pymysql.cursors

def make_connection():
    return pymysql.connect(
        host='reds-lineup.c63ijpxfdwey.us-east-1.rds.amazonaws.com',
        user='admin', 
        passwd='baseball',
        db='reds-offense',
        port=3306)

connect = make_connection()
database = connect.cursor()

# setting up DB Schema

database.execute('DROP DATABASE IF EXISTS reds-offense');
database.execute('CREATE DATABASE reds-offense');
database.execute('USE reds-offense');

database.execute('DROP TABLE IF EXISTS League');
database.execute('DROP TABLE IF EXISTS Reds');
database.execute('DROP TABLE IF EXISTS Catchers');
database.execute('DROP TABLE IF EXISTS FirstBasemen');
database.execute('DROP TABLE IF EXISTS SecondBasemen');
database.execute('DROP TABLE IF EXISTS ThirdBasemen');
database.execute('DROP TABLE IF EXISTS Shortstops');
database.execute('DROP TABLE IF EXISTS Outfielders');

database.execute('''CREATE TABLE League (
    Rank     INT NOT NULL,
    Team     VARCHAR(12) NOT NULL,
    G        INT NOT NULL,
    PA       INT NOT NULL,
    HR       INT NOT NULL,
    R        INT NOT NULL,
    RBI      INT NOT NULL,
    SB       INT NOT NULL,
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
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
    BB%       DECIMAL NOT NULL,
    K%        DECIMAL NOT NULL,
    AVG       DECIMAL NOT NULL,
    OBP       DECIMAL NOT NULL,
    SLG       DECIMAL NOT NULL,
    wOBA      DECIMAL NOT NULL,
    wRC+      INT NOT NULL,
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
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
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
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
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
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
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
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
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
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
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
    BB%      DECIMAL NOT NULL,
    K%       DECIMAL NOT NULL,
    AVG      DECIMAL NOT NULL,
    OBP      DECIMAL NOT NULL,
    SLG      DECIMAL NOT NULL,
    wOBA     DECIMAL NOT NULL,
    wRC+     INT NOT NULL,
    PRIMARY KEY (Rank)
)''');

file_League = open("../League.csv", "r")
file_Reds = open("../Reds.csv", "r")
file_Catchers = open("../Catchers.csv", "r")
file_FirstBasemen = open("../FirstBasemen.csv", "r")
file_SecondBasemen = open("../SecondBasemen.csv", "r")
file_ThirdBasemen = open("../ThirdBasemen.csv", "r")
file_Shortstops = open("../Shortstops.csv", "r")
file_Outfielders = open("../Outfielders.csv", "r")

leagueData = file_League.readlines()
redsData = file_Reds.readlines()
catchersData = file_Catchers.readlines()
firstBasemenData = file_FirstBasemen.readlines()
secondBasemenData = file_SecondBasemen.readlines()
thirdBasemenData = file_ThirdBasemen.readlines()
shortstopsBasemenData = file_Shortstops.readlines()
outfieldersData = file_Outfielders.readlines()

for lines in leagueData:
    print(lines)

database.close()


