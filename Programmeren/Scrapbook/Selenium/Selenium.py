from selenium import webdriver
import page
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from element import BasePageElement
from locators import MainPageLocators

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.hu.nl/')

try:
    terms = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonAccept"))
    )
finally:
    print(terms)