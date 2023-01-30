from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from pathlib import Path

driver = webdriver.Chrome("chromedriver")

def run(driver):
    username='_ujjwal_100'
    pwd='Hi@34ujj'

    driver.get("https://pradan.issdc.gov.in/ch2/protected/payload.xhtml")
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(pwd)
    driver.find_element("name", "login").click()
    driver.find_element("name",'tableForm:payloads:6:j_idt44').click()
    sel=Select(driver.find_element("name",'tableForm:lazyDocTable_rppDD'))
    sel.select_by_visible_text('25')
    driver.find_element("id",'tableForm:lazyDocTable:filename').click()
    time.sleep(15)
    count=0

    path = Path('./pages_done.txt')
    if path.is_file()==False:
        with open('pages_done.txt','w') as f:
            f.write('0')
        with open('links_done1.txt','w') as f:
            f.write('')

    with open('pages_done.txt','r') as f:
        start=f.readline()
    if start!='0':
        page_no = Select(driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/form[3]/div[1]/div[3]/select[1]"))
        page_no.select_by_visible_text(str(int(start)+1))
        time.sleep(45)

    for i in range(int(start),130):
        sel1=driver.find_elements("xpath","//*[@style='color: #00F;']")
        
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('chrome://downloads/')
        driver.switch_to.window(driver.window_handles[0])
        
        for item in sel1:
            count+=1
            if "nc" in item.text:
                item.click()
                with open(f"links_done{i+1}.txt",'a') as f:
                    f.write(item.text+'\n')
            else:
                break

        accessed=set()
        driver.switch_to.window(driver.window_handles[1])
        while True:
            try:
                try:
                    root1 = driver.find_element(By.TAG_NAME,'downloads-manager')
                except:
                    root1 = driver.find_element(By.TAG_NAME,'downloads-manager has-shadow_')
                shadow_root1 = root1.shadow_root

                for i in range(7):
                    root2 = WebDriverWait(driver, 10).until(EC.visibility_of(shadow_root1.find_element(by=By.ID, value=f'frb{i}')))
                    shadow_root2 = root2.shadow_root

                    show = WebDriverWait(driver, 10).until(EC.visibility_of(shadow_root2.find_element(by=By.CSS_SELECTOR, value='[focus-type="show"]')))
                    accessed.add(show.text)
                    print(len(accessed))
                if len(accessed)==25:
                    break
            except:
                try:
                    root1 = driver.find_element(By.TAG_NAME,'downloads-manager')
                except:
                    root1 = driver.find_element(By.TAG_NAME,'downloads-manager has-shadow_')
                shadow_root1 = root1.shadow_root

                for i in range(10):
                    try:
                        root2 = WebDriverWait(driver, 10).until(EC.visibility_of(shadow_root1.find_element(by=By.ID, value=f'frb{i}')))
                        shadow_root2 = root2.shadow_root
                        try:
                            resume = WebDriverWait(driver, 10).until(EC.visibility_of(shadow_root2.find_element(by=By.LINK_TEXT, value=' Resume ')))
                            resume.click()
                            time.sleep(3)
                        except:
                            pass
                    except:
                        pass

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        with open('pages_done.txt','w') as f:
            f.write(str(i+1))
        with open(f"links_done{i+2}.txt",'w') as f:
            f.write('')
        driver.find_element("xpath","//*[@aria-label='Next Page']").click()
        time.sleep(15)

run(driver)
driver.quit()
driver.close()
