class Player:
    def __init__(self, name, position, cost=None, country=None) -> None:
        self.name = name
        self.position = position
        self.country = country
        self.cost = cost
        self.is_benched = False
    
    def __str__(self) -> str:
        return f'{self.name} -- {self.position} -- {self.cost} -- {self.is_benched}'

class Squad:
    def __init__(self, players_on_fantasy, starting_players, matches) -> None:
        self.fantasy = players_on_fantasy
        self.starting = starting_players
        self.matches = matches
        self.selected_players = []
        self.choose_players_vs_italy()
        self.rank_teams()
        self.select_rank2_players()
        self.select_rank3_players()
        self.select_rank4_players()
        self.select_rank5_players()
    
    def choose_players_vs_italy(self):
        selected_team = None
        positions = ['Fullback', 'Wing', 'Fly-half']
        for match in self.matches:
            if match.isItalyPlaying:
                selected_team = match.home_team if match.home_team != 'Italy' else match.away_team
        for player in self.starting:
            if player.country == selected_team and player.position in positions:
                self.selected_players.append(player)
    
    def rank_teams(self):
        rankings = {
            "England": "",
            "France": "",
            "Scotland": "",
            "Wales": "",
            "Ireland": "",
            "Italy": 6
        }
        winning_odds = []
        losing_odds = []
        for match in self.matches:
            if match.isItalyPlaying:
                selected_team = match.home_team if match.home_team != 'Italy' else match.away_team
                rankings[selected_team] = 1
                continue
            if match.is_home_win:
                winning_odds.append((match.home_team, match.home_win_prob))
                losing_odds.append((match.away_team, match.away_win_prob))
            else:
                winning_odds.append((match.away_team, match.away_win_prob))
                losing_odds.append((match.home_team, match.home_win_prob))
        winning_odds.sort(key = lambda x: x[1], reverse=True)
        losing_odds.sort(key = lambda x: x[1], reverse=True)
        for i, odd in enumerate(winning_odds):
            team = odd[0]
            rankings[team] = i+2
        for i, odd in enumerate(losing_odds):
            team = odd[0]
            rankings[team] = i+4
        self.rankings = rankings
            

    def select_rank2_players(self):
        country = list(self.rankings.keys())[list(self.rankings.values()).index(2)]
        positions = ['Centre', 'Back-row', 'Second-row', 'Hooker']
        count = 0
        for player in self.starting:
            if player.country != country:
                continue
            for pos in positions:
                if player.position == pos:
                    count += 1
                    if count > 4: return
                    self.selected_players.append(player)
                    continue

    def select_rank3_players(self):
        country = list(self.rankings.keys())[list(self.rankings.values()).index(3)]
        positions = ['Centre', 'Back-row', 'Second-row', 'Prop']
        count = 0
        for player in self.starting:
            if player.country != country:
                continue
            for pos in positions:
                if player.position == pos:
                    count += 1
                    if count > 4: return
                    self.selected_players.append(player)
                    continue

    def select_rank4_players(self):
        country = list(self.rankings.keys())[list(self.rankings.values()).index(4)]
        positions =  ['Back-row', 'Second-row', 'Prop', 'Hooker']
        count = 0
        for player in self.starting:
                    if player.country != country:
                        continue
                    for pos in positions:
                        if player.position == pos:
                            count += 1
                            if count > 3: return
                            if count == 3: player.is_benched = True
                            self.selected_players.append(player)
                            continue

    def select_rank5_players(self):
        country = list(self.rankings.keys())[list(self.rankings.values()).index(5)]
        positions = ['Scrum-half', 'Back-row', 'Second-row', 'Prop', 'Hooker']
        count = 0
        for player in self.starting:
            if player.country != country:
                continue
            for pos in positions:
                if player.position == pos:
                    count += 1
                    if count > 3: return
                    if count > 1: player.is_benched = True
                    self.selected_players.append(player)
                    continue
    
    def summarise_squad(self):
        for player in self.selected_players:
            print(player)