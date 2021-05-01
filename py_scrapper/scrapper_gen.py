from time import sleep
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lib2to3.pgen2 import driver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

browser.get("https://twitter.com/home")
browser.implicitly_wait(10)

username = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
browser.implicitly_wait(10)
password = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
browser.implicitly_wait(10)
username.send_keys("ayush_tamra")
password.send_keys("")
browser.implicitly_wait(10)
login_button = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
login_button.click()