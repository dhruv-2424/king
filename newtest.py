from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException
import subprocess
import time

print("Script started")

options =  webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to the Chromium binary
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")  # Disable sandboxing
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage



driver = webdriver.Chrome(options=options)

try:
    # Open the webpage
    driver.get("https://bdgame.in/")
except Exception as e:
    print("Element not found:", str(e))


user_name = driver.find_element("id", "username")
user_name.send_keys("king")
time.sleep(5)
user_pass = driver.find_element("id", "password")
user_pass.send_keys("done")
time.sleep(5)
# user_sumbit = driver.find_element(By.XPATH, '/html/body/div[475]/form/button')
user_pass.send_keys(Keys.RETURN)

time.sleep(50)

driver.quit()   
