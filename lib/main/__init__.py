from pathlib import Path
import json

from time import sleep
import random

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_config():
    print("Reading config...")
    dir = Path(__file__).parents[2]
    filename = dir / 'config.json'
    f = open(filename)

    config = json.load(f)

    f.close()
    return config


def run(version):
    print(f"Running v{version}")

    try:
        config = read_config()
    except FileNotFoundError:
        print("Config not found.")

    credentials = config["account_info"]
    dbinfo = config["database_info"]

    try:
        username = credentials["username"]
        password = credentials["password"]

        print("Connecting to MongoDB database")
        database = db(cluster=dbinfo["cluster"],
                      database=dbinfo["database"], username=username)

        options = webdriver.FirefoxOptions()
        options.headless = True  # Toggle Headless Mode

        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(5)

        browser.get('website goes here...')

        home_page = HomePage(browser)
        login_page = home_page.go_to_login_page()
        login_page.login(username, password)
        print("Logged in!")
        home_page.skip_reminders()
        home_page.go_to_profile_page(username=username)

        mainMenu(browser=browser, username=username, database=database)

    except ElementClickInterceptedException:
        print("Invalid Credentials. Please double check the username and password in the config.json file and fix any mistakes. Then proceed to run the program again.")
        browser.close()

        # browser.close()
