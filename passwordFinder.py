from selenium import webdriver
from selenium.webdriver.common.by import By
import re

repo = input (" repo you would like to target")

repo1 = repo
chrome_driver_path = "/Users/HP/Desktop/developer/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver,get(repo)
res = driver.find_elements(By.CLASS_NAME, "repo")
actual_txt_file = []