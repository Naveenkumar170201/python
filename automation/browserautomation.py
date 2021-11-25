from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt=Options()

opt.add_argument('--start-maximized')
browser=webdriver.Chrome(options=opt)
browser.get("https://google.com")