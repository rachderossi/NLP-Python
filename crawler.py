from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.service import Service
import calendar
import time
import locale


s = Service('../chromedriver')
browser = webdriver.Chrome(service=s)
browser.get("here goes the url")
login = browser.find_element(By.NAME, 'login')
login.send_keys('') # here you put your login information
password = browser.find_element(By.NAME, 'password')
password.send_keys('') # here your password
botao = browser.find_element(
    By.CSS_SELECTOR, '[href="javascript:document.form1.submit()"]').click()

elemento = browser.find_element(
    By.CSS_SELECTOR, '[href="main-load?fetch=true&report_type=myReport&userid=2125&timestamp=20221122111457"]').click()

dimensoes = browser.find_element(By.NAME, "cruzamentoDimensoes").click()
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])

div = browser.find_element(By.ID, "dimensionMatrix_0")
div = browser.find_element(By.CSS_SELECTOR, '[value="day"]').click()
div = browser.find_element(By.ID, "dimensionMatrix_4")
div = browser.find_element(
    By.CSS_SELECTOR, '[value="origin_client_desc_h1"]').click()
div = browser.find_element(By.ID, "dimensionMatrix_11")
div = browser.find_element(
    By.CSS_SELECTOR, '[value="transaction_channel_desc_h1"]').click()
div = browser.find_element(By.ID, "dimensionMatrix_13")
div = browser.find_element(
    By.CSS_SELECTOR, '[value="transaction_detail_desc"]').click()
div = browser.find_element(By.NAME, "rec_qty0").click()
div = browser.find_element(By.NAME, "rec_amt0_money").click()
div = browser.find_element(By.ID, "button_ok").click()

WebDriverWait(browser, 60).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/table/tbody/tr[2]/td/div/span/a[1]"))).click()
browser.switch_to.window(browser.window_handles[0])
