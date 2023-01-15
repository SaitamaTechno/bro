from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

import time
import json

options = Options()
#options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.tradingview.com/chart/45CxtJik/")
print(driver.title)
actions = ActionChains(driver)

link1=driver.find_element(By.CLASS_NAME, "js-login-link")
link1.click()
time.sleep(2)
link1=driver.find_elements(By.CLASS_NAME, "tv-social__title")
link1[1].click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
link1=driver.find_element(By.NAME, "email")
link1.send_keys("jackystinson1453@gmail.com")
link1=driver.find_element(By.NAME, "pass")
link1.send_keys("aGzansicim.7274")
link1.send_keys(Keys.RETURN)
driver.switch_to.window(driver.window_handles[0])
time.sleep(30)
print("SÜRE BAŞLADI!")
a=0
ta=60
for a in range(ta):
    print(ta-a)
    time.sleep(1)
    a+=1
print("SÜRE BİTTİ!")
data="""{}"""
data= json.loads(data)
jsondata={"date":[],
         "open":[],
         "high":[],
         "low":[],
         "close":[],
         "change":[]}
datelist=[]
openlist=[]
highlist=[]
lowlist=[]
closelist=[]
changelist=[]
while 1:
    while 1:
        try:
            date=driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/span")
            date=date.text
            openn=driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/span")
            openn=float(openn.text)
            high=driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/span")
            high=float(high.text)
            low=driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]/span")
            low=float(low.text)
            closee=driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[4]/div[2]/span")
            closee=float(closee.text)
            change=driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[2]/span")
            change=change.text
            break
        except StaleElementReferenceException or WebDriverException:
            time.sleep(0.001)
    datelist.append(date)
    openlist.append(openn)
    highlist.append(high)
    lowlist.append(low)
    closelist.append(closee)
    changelist.append(change)
    tablo=driver.find_element(By.TAG_NAME, 'body')
    tablo.send_keys(Keys.RIGHT)
    if date=="Fri 13 Jan '23":
        break
jsondata["date"]+= datelist
jsondata["open"]+= openlist
jsondata["high"]+= highlist
jsondata["low"]+= lowlist
jsondata["close"]+= closelist
jsondata["change"]+= changelist
data.update(jsondata)
newjsondata=json.dumps(data)

f=open("GBPUSD.json", "w")
a=json.dump(newjsondata, f)
f.close()

print("Process Completed!")
