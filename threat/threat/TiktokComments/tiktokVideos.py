from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_all_tiktoks(uri):
    service = Service(executable_path="/Users/aadit/Documents/GitHub/TiktokResearch1/TikTokAPITesting/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get(uri)

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-1g95xhm-AVideoContainer"))
    )

    element = driver.find_elements(By.CLASS_NAME, "css-1g95xhm-AVideoContainer")

    data = []
    for el in element:
        link = el.get_attribute("href")
        data.append(link)
        print(link)

    driver.quit()

    return data

