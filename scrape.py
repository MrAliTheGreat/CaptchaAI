from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import time, sleep
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


def getNewImageName():
    return len(os.listdir("./Unannotated-Dataset")) + 1    

def capture(chrome: webdriver):
    with open(f"./Unannotated-Dataset/{getNewImageName()}.png", mode = "wb") as img:
        img.write(
            WebDriverWait(chrome, 30).until(
                EC.visibility_of_element_located((
                    By.ID, os.environ.get("IMG_ID")         
                ))
            ).screenshot_as_png
        )
    print(f"New image added at {datetime.now()}!")

def renewImage(chrome: webdriver):
    chrome.find_element(
        By.ID, os.environ.get("RELOAD_ID")
    ).click()


start = time()
wait = 6
options = Options()
options.add_argument("--headless=new")
chrome = webdriver.Chrome("./chromedriver.exe", options = options)
chrome.maximize_window()
chrome.implicitly_wait(10)
chrome.get(os.environ.get("URL"))

while(True):
    if(not len(os.listdir('./Unannotated-Dataset')) % 50):
        chrome.refresh()
    capture(chrome)
    renewImage(chrome)
    print(f"{len(os.listdir('./Unannotated-Dataset'))} Images in Unannotated Dataset!")
    sleep( wait - ((time() - start) % wait) )