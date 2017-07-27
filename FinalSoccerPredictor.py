import numpy as np

# Loads all data
PremierData = np.loadtxt('./PremierSoccerData.txt', delimiter="|",
                         dtype={"names":  ["identifier", "name", "wins", "losses", "ranking", "goals", "rating"],
                      "formats": [np.int, "S128", np.int, np.int, np.int, np.int, np.float]})

PremierScores = np.loadtxt('./PremierSoccerScores.txt', delimiter="\t",
                         dtype={"names":  ["team one", "one score", "two score", "team two"],
                      "formats": ["S128", np.int, np.int, "S128"]})

LaLigaData = np.loadtxt('./LaLigaSoccerDatatxt.txt', delimiter="|",
                        dtype={"names":  ("identifier", "name", "wins", "losses", "ranking", "goals", "rating"),
                      "formats": (np.int, "S128", np.int, np.int, np.int, np.int, np.float)})

LaLigaScores = np.loadtxt('./LaLigaSoccerScores.txt', delimiter="\t",
                         dtype={"names":  ["team one", "one score", "two score", "team two"],
                      "formats": ["S128", np.int, np.int, "S128"]})

SeriesAData = np.loadtxt('./SeriesASoccerData.txt', delimiter="|", dtype={"names":  ["identifier", "name", "wins", "losses", "ranking", "goals", "rating"],
                      "formats": [np.int, "S128", np.int, np.int, np.int, np.int, np.float]})

SeriesAScores = np.loadtxt('./SeriesASoccerScores.txt', delimiter="\t",
                         dtype={"names":  ["team one", "one score", "two score", "team two"],
                      "formats": ["S128", np.int, np.int, "S128"]})

print "Welcome to Soccer Predictor"

# Function used for predictions (used for every league)
def Predictor(a, b, c, d):
    # finds line with the data and saves it as a variable
    for line in c:
        if a in line:
            idone = line

    for lines in c:
        if b in lines:
            idtwo = lines

    # sets variable and keeps track of superior team
    ascore = 0
    bscore = 0

    awinloss = idone[2]/idone[3]
    bwinloss = idtwo[2]/idtwo[3]

    # compares the win loss ratio
    if awinloss > bwinloss:
        ascore += 1
    else:
        bscore += 1
    # compares the teams overall ranking
    if idone[4]<idtwo[4]:
        ascore += 1
    else:
        bscore += 1
    # compares the number of goals they scored
    if idone[5]>idtwo[5]:
        ascore += 1
    else:
        bscore += 1
    # compares their rating (0-5) star
    if idone[6]>idtwo[6]:
        ascore += 1
    else:
        bscore += 1

    # looks at which team is overall better
    if ascore>bscore:
        print "Based on statistics %s is the team that will probably win!" % a
    if bscore>ascore:
        print "Based on statistics %s is the team that will probably win!" % b
    if ascore == bscore:
        print "Based on statistics it will probably be a draw between %s and %s" % (a, b)

    # Predicts the score
    onesav = []
    twosav = []
    combo = [a, b]
    for linex in d:
        if (combo[0] in linex["team one"] or combo[0] in linex["team two"]) and (
                combo[1] in linex["team one"] or combo[1] in linex["team two"]):
            game = linex
            if combo[0] in game["team one"]:
                onesav.append(game["one score"])
            else:
                onesav.append(game["two score"])
            if combo[1] in game["team one"]:
                twosav.append(game["one score"])
            else:
                twosav.append(game["two score"])

    scoreone = round(float(np.sum(onesav)) / len(onesav))
    scoretwo = round(float(np.sum(twosav)) / len(twosav))
    print "According to previous games, the score will be %s : %d to %s : %d" % (a, scoreone, b, scoretwo)

# Asks user for input of league and teams
League = raw_input("Enter a league to start: ")

# Checks if the league is valid
league_list = ["Premier League", "La Liga", "Series A"]
while League not in league_list:
    print "Invalid league"
    League = raw_input("Enter a league to start: ")

# Sets variables to correct data sets
if League == "Premier League":
    c = PremierData
    d = PremierScores
if League == "La Liga":
    c = LaLigaData
    d = LaLigaScores
if League == "Series A":
    c = SeriesAData
    d = SeriesAScores

# Asks user to enter first team name
a = raw_input("Enter the name of the first team from the league: ")
# Checks if team name in database
while a not in c['name']:
    print "Invalid team"
    a = raw_input("Enter the name of the first team from the league: ")

# Asks user to enter second team name
b = raw_input("Enter the name of the second team from the league: ")
# Checks if team name in database
while b not in c['name']:
    print "Invalid team"
    b = raw_input("Enter the name of the first team from the league: ")

# Calls the functions in order to find the winning team in the right league
Predictor(a, b, c, d)

