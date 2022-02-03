class Match:
    def __init__(self, home_team, away_team, home_odds, draw_odds, away_odds) -> None:
        self.home_team = home_team
        self.away_team = away_team
        self.home_odds = home_odds # odds are in the form "1/6" for example. Put in 6 pounds, get 1 pound profit. 
        self.draw_odds = draw_odds
        self.away_odds = away_odds
        self.calc_winning_probabilities()
        self.winning_team = self.determine_winning_team()
 
    def __str__(self) -> str:
        return f"{self.home_team} (Home) vs {self.away_team} (Away)"

    def calc_winning_probabilities(self):
        home_odds = self.home_odds.split('/')
        away_odds = self.away_odds.split('/')
        self.home_win_prob = float(home_odds[1])/float(home_odds[0])
        self.away_win_prob = float(away_odds[1])/float(away_odds[0])

    def determine_winning_team(self):
        if self.home_win_prob > self.away_win_prob:
            return self.home_team
        else: 
            return self.away_team
    
    def summarise_match(self):
        if self.winning_team == self.home_team:
            print(f"{self.winning_team} expected to win against {self.away_team}. Probability of {self.home_win_prob:.2f} vs {self.away_win_prob:.2f}")
        if self.winning_team == self.away_team:
            print(f"{self.winning_team} expected to win against {self.home_team}. Probability of {self.away_win_prob:.2f} vs {self.home_win_prob:.2f}")
            