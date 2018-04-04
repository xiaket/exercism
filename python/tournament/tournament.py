#!/usr/bin/env python
#encoding=utf8

class Team(object):
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.loss = 0
        self.draw = 0

    @property
    def score(self):
        return 3 * self.win + self.draw

    @property
    def games(self):
        return self.win + self.loss + self.draw

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name

    def __repr__(self):
        return "<Team {}>".format(self.name)

def tally(results):
    teams = {team: Team(team)
        for line in results.splitlines()
        for team in line.split(";")[:2]
    }
    for line in results.splitlines():
        team1, team2, result = line.split(";")
        if result == 'win':
            teams[team1].win +=1
            teams[team2].loss +=1
        elif result == 'draw':
            teams[team1].draw +=1
            teams[team2].draw +=1
        else:
            teams[team2].win +=1
            teams[team1].loss +=1
    teams = list(teams.values())
    teams.sort(reverse=True)

    header = 'Team                           | MP |  W |  D |  L |  P'
    lines = [header]
    for team in teams:
        line = "|".join([
            team.name.ljust(31), '{0: 3d} '.format(team.games),
            '{0: 3d} '.format(team.win), '{0: 3d} '.format(team.draw),
            '{0: 3d} '.format(team.loss), '{0: 3d}'.format(team.score),
        ])
        lines.append(line)
    return '\n'.join(lines)
