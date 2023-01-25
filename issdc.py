from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("chromedriver")

def run(driver):
    username='*******'
    pwd='********'

    driver.get("https://pradan.issdc.gov.in/ch2/")
    driver.find_element("link text",'BrowseAndDownload').click()
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(pwd)
    driver.find_element("name", "login").click()
    driver.find_element("name",'tableForm:payloads:6:j_idt44').click()
    sel=Select(driver.find_element("name",'tableForm:lazyDocTable_rppDD'))
    sel.select_by_visible_text('25')
    driver.find_element("id",'tableForm:lazyDocTable:filename').click()
    # tableForm:lazyDocTable:label_-_Product_Observational_-_Observation_Area_-_Time_Coordinates_-_start_date_time
    time.sleep(20)
    count=0
    for i in range(130):
        sel1=driver.find_elements("xpath","//*[@style='color: #00F;']")
        for item in sel1:
            count+=1
            if 'nc' in item.text:
                print(item.text)
                item.click()
            else:
                break
            if count==25:
                count=0
                driver.find_element("xpath","//*[@aria-label='Next Page']").click()
                time.sleep(1400)
    n=int(input("ENter:"))

run(driver)
driver.close()
