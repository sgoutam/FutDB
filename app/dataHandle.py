__author__ = 'Rahul'
from pymongo import MongoClient
from request import newsrequest
from TextSummarize import wiki_scrape

class TeamResponse:
    def __init__(self, Name, Position, League, Games , Points,newsresponses):
        self.type = 'team'
        self.league = League
        self.name = Name
        self.year = 2015
        self.position = Position
        self.games = Games
        self.points = Points
        self.newsresponses = newsresponses

class PlayerResponse:
    def __init__(self, Name, Number, Club, years, DOB, Team, Position, newsresponses):
        self.type = 'player'
        self.club = Club
        self.name = Name
        self.number = Number
        self.years = years
        self.DOB = DOB
        self.team = Team
        self.position = Position
        self.newsresponses = newsresponses

from pymongo import MongoClient
client = MongoClient()
db = client['football']




def eplteams(query):
    teamresponse = TeamResponse('','','','','','')
    docs = db['EPLStandings'].find({"teamName": query})

    for doc in docs:

        narr = newsrequest(doc['teamName'])
        teamresponse = TeamResponse(doc['teamName'],doc['position'],'EPL',20,doc['points'],narr)

    return teamresponse


def worldcupplayers(query):
    years = []
    docs = db['WorldCupPlayers'].find({"FullName": query})

    i=0

    playerresponse = PlayerResponse('','','','','','','','')
    for doc in docs:
        years.append(doc['Year'])
        i=i+1
        if i==(docs.count()):
            narr = newsrequest(doc['FullName'])
            playerresponse = PlayerResponse(doc['FullName'],
                                    doc['Number'],
                                    doc['Club'],
                                    years,
                                    doc['DateOfBirth'],
                                    doc['Team'],
                                    doc['Position'],
                                    narr)


    return playerresponse


