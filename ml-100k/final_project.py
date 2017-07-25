import numpy as np

PremierData = np.loadtxt('./premier_league.txt', delimiter="|",
                         dtype={"names":  ["identifier", "name", "wins", "losses", "ranking", "goals", "rating"],
                                "formats": [np.int, "S128", np.int, np.int, np.int, np.int, np.float]})

LaLigaData = np.loadtxt('./la_liga.txt', delimiter="|",
                        dtype={"names":  ("identifier", "name", "wins", "losses", "ranking", "goals", "rating"),
                               "formats": (np.int, "S128", np.int, np.int, np.int, np.int, np.float)})

SeriesAData = np.loadtxt('./serie_a_league.txt', delimiter="|", dtype={"names":  ["identifier", "name", "wins", "losses", "ranking", "goals", "rating"],
                                                                                  "formats": [np.int, "S128", np.int, np.int, np.int, np.int, np.float]})

print "Welcome to Soccer Predictor"

# Premier League Predictor
def PremierPredictor(a, b):
    # finds line with the data and saves it as a variable
    for line in PremierData:
        if a in line:
            idone = line

    for lines in PremierData:
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
        print "%s is the team that will win!" % a
    if bscore>ascore:
        print "%s is the team that will win!" % b
    if ascore == bscore:
        print "It will probably be a draw between %s and %s" % (a, b)

# La Liga Prediction
def LaLigaPredictor(a, b):
    # finds line with the data and saves it as a variable
    for line in LaLigaData:
        if a in line:
            idones = line

    for lines in LaLigaData:
        if b in lines:
            idtwos = lines

    # sets variable and keeps track of superior team
    ascore = 0
    bscore = 0

    awinloss = idones[2]/idones[3]
    bwinloss = idtwos[2]/idtwos[3]

    # compares the win loss ratio
    if awinloss > bwinloss:
        ascore += 1
    else:
        bscore += 1
    # compares the teams overall ranking
    if idones[4]<idtwos[4]:
        ascore += 1
    else:
        bscore += 1
    # compares the number of goals they scored
    if idones[5]>idtwos[5]:
        ascore += 1
    else:
        bscore += 1
    # compares their rating (0-5) star
    if idones[6]>idtwos[6]:
        ascore += 1
    else:
        bscore += 1

    # looks at which team is overall better
    if ascore>bscore:
        print "%s is the team that will win!" % a
    if bscore>ascore:
        print "%s is the team that will win!" % b
    if ascore == bscore:
        print "It will probably be a draw between %s and %s" % (a, b)

# Series A Predition
def SeriesAPredictor(a, b):
    # finds line with the data and saves it as a variable
    for line in SeriesAData:
        if a in line:
            idoness = line

    for lines in SeriesAData:
        if b in lines:
            idtwoss = lines

    # sets variable and keeps track of superior team
    ascore = 0
    bscore = 0

    awinloss = idoness[2]/idoness[3]
    bwinloss = idtwoss[2]/idtwoss[3]

    # compares the win loss ratio
    if awinloss > bwinloss:
        ascore += 1
    else:
        bscore += 1
    # compares the teams overall ranking
    if idoness[4]<idtwoss[4]:
        ascore += 1
    else:
        bscore += 1
    # compares the number of goals they scored
    if idoness[5]>idtwoss[5]:
        ascore += 1
    else:
        bscore += 1
    # compares their rating (0-5) star
    if idoness[6]>idtwoss[6]:
        ascore += 1
    else:
        bscore += 1

    # looks at which team is overall better
    if ascore>bscore:
        print "%s is the team that will win!" % a
    if bscore>ascore:
        print "%s is the team that will win!" % b
    if ascore == bscore:
        print "It will probably be a draw between %s and %s" % (a, b)

# Asks user for input of league and teams
League = raw_input("Enter a league to start: ")
a = raw_input("Enter the name of the first team from the league: ")
b = raw_input("Enter the name of the second team from the league: ")

# Calls the functions in order to find the winning team in the right league
if League == "Premier League":
    PremierPredictor(a, b)
if League == "La Liga":
    LaLigaPredictor(a, b)
if League == "Series A":
    SeriesAPredictor(a, b)
