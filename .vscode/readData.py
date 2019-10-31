import csv

file_League = open("../League.csv", "r")
file_Reds = open("../Reds.csv", "r")
file_Catchers = open("../Catchers.csv", "r")
file_FirstBasemen = open("../FirstBasemen.csv", "r")
file_SecondBasemen = open("../SecondBasemen.csv", "r")
file_ThirdBasemen = open("../ThirdBasemen.csv", "r")
file_Shortstops = open("../Shortstops.csv", "r")
file_Outfielders = open("../Outfielders.csv", "r")

leagueData = csv.reader(file_League, delimiter=',')
redsData = file_Reds.readlines()
catchersData = file_Catchers.readlines()
firstBasemenData = file_FirstBasemen.readlines()
secondBasemenData = file_SecondBasemen.readlines()
thirdBasemenData = file_ThirdBasemen.readlines()
shortstopsBasemenData = file_Shortstops.readlines()
outfieldersData = file_Outfielders.readlines()


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
    print(lines)