from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from skpy import Skype
import pandas as pd
username = 'sudarshan.jaikrishnan@infrastack-labs.com'
password = 'Hubble@123'
website = 'https://monitor.hubble.in/d/lF0jFkrZz/isl-hubble?orgId=1&refresh=1m&from=now-1h&to=now'
path = 'C:\\Users\\Admin\\Downloads\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

driver.find_element(By.NAME, "user").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//span[text()='Log in']").click()


time.sleep(10)
#WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.NAME,"user")))

#dashboardContent = driver.find_element(By.CLASS_NAME, 'dashboard-content')

#dashboardContentList = driver.find_elements(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]')
#print(len(dashboardContentList))

#for item in dashboardContentList:
#    span = item.find_element(By.XPATH, "//div/div[1]/div/div[1]/div/div/span")
#    print(span.text)

dashboardContent = driver.find_element(By.CLASS_NAME, 'dashboard-content')
ApiLatency: WebElement = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/plugin-component/panel-plugin-singlestat/grafana-panel/ng-transclude/div/div[1]/span/span')
print(ApiLatency.text)

dashboardContent = driver.find_element(By.CLASS_NAME, 'dashboard-content')
CSLatency = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[19]/div/div[1]/div/div[2]/div/plugin-component/panel-plugin-singlestat/grafana-panel/ng-transclude/div/div[1]/span/span')
print(CSLatency.text)

slogin = Skype("infrastack@protonmail.com", "Skype@123")

contact = slogin.contacts["live:bokadiayashwant"]
msg=f"api latency is - {str(ApiLatency.text)}\n" \
    f"cs latency is - {str(CSLatency.text)}\n"
contact.chat.sendMsg(msg)

