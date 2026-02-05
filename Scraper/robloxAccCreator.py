from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import random
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.roblox.com/signup")

time.sleep(5)

try:
    # https://www.selenium.dev/documentation/webdriver/support_features/select_lists/
    monthDropdown = Select(driver.find_element(By.ID, "MonthDropdown"))
    monthDropdown.select_by_value("Jan")

    dayDropdown = Select(driver.find_element(By.ID, "DayDropdown"))
    dayDropdown.select_by_value("01")

    yearDropdown = Select(driver.find_element(By.ID, "YearDropdown"))
    yearDropdown.select_by_value("2000")

    usernameInput = driver.find_element(By.ID, "signup-username")
    usernameInput.send_keys("adrianchen{}".format(random.randint(10000, 100000)))

    passwordInput = driver.find_element(By.ID, "signup-password")
    passwordInput.send_keys("adrianissodumb123")

    input()

except Exception    as e:
    print("Something went wrong: {}. Figure it out...".format(e))