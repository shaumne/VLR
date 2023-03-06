from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_drvier(args:str):
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get(f"https://www.vlr.gg/search/?q={args}&type=players")
  return driver

def get_stat_url(name:str):
    driver = get_drvier(name)
    player = driver.find_element(by="xpath", value="/html/body/div[5]/div[1]/div/div[2]/a")
    player.click()
    url = f"{driver.current_url}/?timespan=all"
    return url