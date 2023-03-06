from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

def get_drvier(args:str):
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_argument('--headless')

  driver = webdriver.Chrome(options=options)
  driver.get(f"https://www.vlr.gg/search/?q={args}&type=teams")
  return driver

def main(args:str):
    
    
    driver = get_drvier(args)
    element = driver.find_element(by="xpath", value="/html/body/div[5]/div[1]/div/div[2]/a")
    element.click()
    
    
    url = driver.current_url
    
    print(url)
    
    return url

