from asyncio import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlsxwriter
import time
#-------------------
nameOfInputFile = "automationForm/DS.txt"

arr_HD= []
f = open(nameOfInputFile)
for line in f:   
    arr_HD.append(line.replace("\n",""))
f.close()

driver = webdriver.Chrome()
driver.get("https://forms.gle/QifYJgMSfyrHrwee6")
driver.maximize_window()

driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div').click()
time.sleep(6)
driver.find_elements(By.CSS_SELECTOR,'li.x-boundlist-item')[0].click()
time.sleep(1)

driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/table/tbody/tr[17]/td/div').click()
time.sleep(1)
thang = driver.find_element(By.NAME,'thang')
count = 1
