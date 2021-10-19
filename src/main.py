import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser=webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()
browser.get('https://www.instagram.com/')
username=browser.find_elements_by_name('username')
password=browser.find_elements_by_name('password')