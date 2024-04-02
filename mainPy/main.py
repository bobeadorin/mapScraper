from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getDayByNumber import getDayByNumber
import re

def getPopularTimesData(url) -> dict:
    PATH : str = r"E:\Programare\Python\mapScraper\mainPy\chromedriver.exe"
    options = Options()
    service  = Service(PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    popularTimesData : list = []
    dayInfo : dict = {
        "day" :'',
        "data" : []
    }
    
    element = driver.find_element(By.CSS_SELECTOR, '[jsname="b3VHJd"]')
    if element: 
        element.click()
    
    wait = webdriver.support.ui.WebDriverWait(driver, 3)

    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    counter = 0

    popularTimes = driver.find_elements(By.CLASS_NAME,"g2BVhd ")
    busy_lvl = None
    time_str = None
    if(popularTimes):
        for time_container in popularTimes:
            time_divs = time_container.find_elements(By.CLASS_NAME, "dpoVLd")
            dayInfo ={
                "id":counter,
                "day" :'',
                "data" : []
            }
            counter+=1
            dayInfo["day"] = getDayByNumber(counter)
            for time_div in time_divs:
                aria_label = time_div.get_attribute('aria-label')
                if " la " in aria_label:
                    busy_lvl, time_str = aria_label.split(" la ")
                else:
                    print("Unexpected format in aria_label:", aria_label)
                busy_lvl = busy_lvl.strip()
                time_str = time_str.strip(".")


                busy_lvl_numbers = re.findall(r'\d+', busy_lvl)
                busy_lvl_numbers_str = ''.join(busy_lvl_numbers)
                busy_lvl_numbers_int = int(busy_lvl_numbers_str)
                busy_lvl_numbers_int = int(busy_lvl_numbers_str)

                dayInfo["data"].append({
                    "busyLvl": busy_lvl_numbers_int,
                    "time": time_str,
                })
            popularTimesData.append(dayInfo)
           

    return  popularTimesData

