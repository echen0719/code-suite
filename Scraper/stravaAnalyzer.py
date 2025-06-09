from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.strava.com/clubs/1326039/members?page=5")
time.sleep(100)