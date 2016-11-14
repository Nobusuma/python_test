import os
from selenium  import webdriver

chromedriver = "/Users/Gonzalo Cattini/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
testDriver = webdriver.Chrome(chromedriver)
