import json

class Player:
    def __init__(self, name: str, nat: str, ass: int, goal: int, pen: int, team: str, game: int):
        self._name = name
        self._nationality = nat
        self._assist = ass
        self._goal = goal
        self._penalty = pen
        self._team = team
        self._games = game
    
    def __str__(self):
        d = 21 - len(self.name)
        if self.goals < 10:
            g = f" {self.goals}"
        else:
            g = self.goals
        if self.assists < 10:
            a = f" {self.assists}"
        else:
            a = self.assists
        if self.point() < 10 :
            c = f"  {self.point()}"
        elif 10 <= self.point() < 100 :
            c = f" {self.point()}"
        else :
            c = self.point()
        
        return f"{self.name}{' ' * d}{self.team}  {g} + {a} = {c}"
    
    def __repr__(self) -> str:
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def nationality(self):
        return self._nationality
    
    @property
    def assists(self):
        return self._assist
    
    @property
    def goals(self):
        return self._goal
    
    @property
    def penalty(self):
        return self._penalty
    
    @property
    def team(self):
        return self._team
    
    @property
    def games(self):
        return self._games

    def point(self):
        return (self.goals + self.assists)

class NHLdb:
    def __init__(self):
        self._players = []
    
    def add(self, player: Player):
        self._players.append(player)
    
    @property
    def players(self):
        return self._players
    
    def number_of_players(self):
        return len(self._players)
    
    def player(self, name: str):
        for p in self.players:
            if p.name == name:
                return p
    
    def teams(self):
        return sorted(list(set([p.team for p in self.players])))
    
    def countries(self):
        return sorted(list(set([p.nationality for p in self.players])))

    def teamlist(self, team: str):
        x = [p for p in self.players if p.team == team]
        x = sorted(x, key= lambda p: p.point(), reverse=True)
        return x
    
    def countrylist(self, country: str):
        x = [p for p in self.players if p.nationality == country]
        x = sorted(x, key= lambda p: p.point(), reverse=True)
        return x

    def best_by_points(self, number: int):
        sort_by_points = sorted(self.players, key= lambda p:(p.point(), p.goals), reverse=True)
        return sort_by_points[0:number]
    
    def best_by_goals(self, number: int):
        sort_by_goals = sorted(self.players, key= lambda p:(p.goals, -p.games), reverse=True)
        return sort_by_goals[0:number]

class FileHandler:
    def __init__(self, nhl: NHLdb):
        self.__nhl = nhl
    
    def load(self, filename: str):
        with open(filename) as f:
            data = f.read()
        players = json.loads(data)
        self.datatransfer(players)
    
    def datatransfer(self, players: list):
        for p in players:
            x = Player(p["name"], p["nationality"], p["assists"], p["goals"], p["penalties"],
                        p["team"], p["games"] )
            self.__nhl.add(x)

class NHLApp:
    def __init__(self, loader: FileHandler, db: NHLdb):
        self._loader = loader
        self._db = db
    
    def _loadfunc(self, fn: str):
        self._loader.load(fn)
        print(f"read the data of {self._db.number_of_players()} players")

    def menu(self):
        print()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def _player(self):
        name = input("name: ")
        p = self._db.player(name)
        print(p)

    def _teams(self):
        list_of_teams = self._db.teams()
        for team in list_of_teams:
            print(team)
        
    def _countries(self):
        list_of_countries = self._db.countries()
        for c in list_of_countries:
            print(c)
    
    def _players_by_team(self):
        team_name = input("team: ")
        team = self._db.teamlist(team_name)
        print()
        for p in team :
            print(p)

    def _players_by_country(self):
        c_name = input("country: ")
        country = self._db.countrylist(c_name)
        print()
        for p in country:
            print(p)
    def _most_points(self):
        hm = int(input("how many: "))
        best_by_points = self._db.best_by_points(hm)
        for p in best_by_points:
            print(p)

    def _most_goals(self):
        hm = int(input("how many:"))
        best_by_goals = self._db.best_by_goals(hm)
        for p in best_by_goals:
            print(p)

    def start(self):
        filename = input("file name: ")
        self._loadfunc(filename)
        self.menu()
        while True:
            print()
            cmd = input("command: " )

            if cmd == "0":
                break
            if cmd == "1":
                self._player()
            if cmd == "2":
                self._teams()
            if cmd == "3":
                self._countries()
            if cmd == "4":
                self._players_by_team()
            if cmd == "5":
                self._players_by_country()
            if cmd == "6":
                self._most_points()
            if cmd == "7":
                self._most_goals()


nhl = NHLdb()
fn = FileHandler(nhl)
ui = NHLApp(fn, nhl)
ui.start()
