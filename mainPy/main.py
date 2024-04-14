from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getDayByNumber import getDayByNumber
import re
from time import sleep

def getPopularTimesData(url) -> dict:
    #<setup> scrapper initialisation , varible declaration ,etc ------------------------------------------------------
    CHROMEDRIVER_PATH : str = r"E:\Programare\Python\mapScraper\mainPy\chromedriver.exe"
    options = Options()
    service  = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    popularTimesData : list = []
    dayInfo : dict = {
        "day" :'',
        "data" : []
    }
    #</setup>---------------------------------------------------------------------------------------------------------

    #<allowCookies> when first connecting to a maps page , the driver should click on the accept cookies button 
    element = driver.find_element(By.CSS_SELECTOR, '[jsname="b3VHJd"]')

    if element: 
        element.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "g2BVhd")))
    
    #</allowCookies> 

    counter = 0 # counter for the getDayByNumber function , to convert numbers into valid Days

    #<findDivWithBusyTimeData> --------------------------------------------------------------------------------------

    popularTimes = driver.find_elements(By.CLASS_NAME,"g2BVhd ")
    busy_lvl = None
    time_str = None

    #</findDivWithBusyTimeData> --------------------------------------------------------------------------------------
 

    if(popularTimes):
        for time_container in popularTimes:
            time_divs = time_container.find_elements(By.CLASS_NAME, "dpoVLd") #finds element that contains the busy lvl data 
            dayInfo ={
                "id":counter,
                "day" :'',
                "data" : []
            }
            counter+=1
            dayInfo["day"] = getDayByNumber(counter)
            for time_div in time_divs:
                aria_label = time_div.get_attribute('aria-label') #busy time data is stored in an aria-label html property
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
