class Match:
    def __init__(self, home_team, away_team, home_odds, draw_odds, away_odds) -> None:
        self.home_team = home_team
        self.away_team = away_team
        self.home_odds = home_odds
        self.draw_odds = draw_odds
        self.away_odds = away_odds
    
    def __str__(self) -> str:
        return f"{self.home_team} (Home) vs {self.away_team} (Away)"

    def determine_winning_team():
        pass