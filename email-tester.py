import xlrd
from selenium import webdriver
import pdb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import re

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)

driver.get("http://mailtester.com/testmail.php")
assert "MailTester" in driver.title

workbook = xlrd.open_workbook("data.xlsx")
worksheet = workbook.sheet_by_name('Sheet1')
for current_row in range(worksheet.nrows):
    email_address = str(worksheet.row(current_row)[0]).partition('\'')[-1].rpartition('\'')[0]
    delay = 6
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        elem = driver.find_element_by_xpath("//input[@name='email']")
        elem.clear()
        elem.send_keys(str(email_address))
        elem.send_keys(Keys.RETURN)
        # driver.find_element_by_xpath("//input[@name='action']").click()
        # driver.find_element_by_css_selector(".button").click()
        delay = 6 # seconds
        time.sleep(3)
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
            # print "Page is ready!"
        except TimeoutException:
            ""
            # print "Loading took too much time!"

        time.sleep(4)
        text="E-mail address is valid"

        try:
            driver.find_elements_by_xpath("//*[contains(text(), 'valid')]")
            # driver.find_element_by_xpath("//*[text='E-mail address is valid']")
            test_variable = "valid"
        except NoSuchElementException:
            test_variable = "not-valid"
        # test_variable = driver.getPageSource().contains(text);
        print email_address, test_variable
    except TimeoutException:
        ""
