from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv
from classes.match import Match

load_dotenv()
PATH_TO_CHROMEDRIVER = os.getenv('PATH_TO_CHROMEDRIVER')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def run():
    print('Running main script...')
    driver = webdriver.Chrome(executable_path=PATH_TO_CHROMEDRIVER)
    driver.get("https://www.oddschecker.com/rugby-union/six-nations")
    sleep(3)
    print('----processing----')
    
    # find the teams that are playing each other
    teams = driver.find_elements_by_class_name("fixtures-bet-name")
    teams_text = [team.text for team in teams]
    teams_lists = []
    for i in range(0, len(teams_text), 2):
        chunk = teams_text[i:i + 2]
        teams_lists.append(chunk)

    # find the betting odds of home win, draw, or away win
    odds = driver.find_elements_by_class_name("add-to-bet-basket")
    odds_text = [odd.text for odd in odds]
    odds_lists = []
    for i in range(0, len(odds_text), 3):
        chunk = odds_text[i:i + 3]
        odds_lists.append(chunk)

    matches = []
    for teams_playing, odds_strings in zip(teams_lists, odds_lists):
        match = Match(teams_playing[0], teams_playing[1], odds_strings[0], odds_strings[1], odds_strings[2])
        match.summarise_match()
        matches.append(match)

    # login to the six nations fantasy and scrape all players
    driver.get("https://fantasy.sixnationsrugby.com/#/welcome/login")
    sleep(3)
    email_input = driver.find_element_by_css_selector('[type|="email"]')
    email_input.click()
    email_input.send_keys(EMAIL)
    password_input = driver.find_element_by_css_selector('[type|="password"]')
    password_input.click()
    password_input.send_keys(PASSWORD)
    submit_btn = driver.find_element_by_css_selector('[type|="submit"]')
    driver.execute_script("arguments[0].click();", submit_btn)
    sleep(3)

    print('----finished processing----')
    driver.quit()

if __name__ == '__main__':
    run()
