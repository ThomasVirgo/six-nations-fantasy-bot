from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

import os
from dotenv import load_dotenv
load_dotenv()
PATH_TO_CHROMEDRIVER = os.getenv('PATH_TO_CHROMEDRIVER')


def run():
    print('Running main script...')
    driver = webdriver.Chrome(executable_path=PATH_TO_CHROMEDRIVER)
    driver.get("https://www.oddschecker.com/rugby-union/six-nations")
    sleep(3)
    print('----processing----')
    teams = driver.find_elements_by_class_name("fixtures-bet-name")
    for team in teams:
        print(team.text)
    odds = driver.find_elements_by_class_name("add-to-bet-basket")
    for odd in odds:
        print(odd.text)
    print('----finished processing----')
    driver.quit()

if __name__ == '__main__':
    run()
