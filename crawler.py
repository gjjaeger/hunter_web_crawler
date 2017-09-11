from selenium import webdriver
import pdb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)

driver.get("https://hunter.io/")
assert "Hunter" in driver.title
driver.find_element_by_xpath("//a[contains(.,'Log in')]").click();
delay = 6 # seconds
time.sleep(8)
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'email-field')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
time.sleep(8)
elem = driver.find_element_by_id("email-field")
elem.clear()
elem.send_keys("gauffreysmithhh1@gmail.com")
elem2 = driver.find_element_by_id("password-field")
elem2.clear()
elem2.send_keys("gjjaeger")
driver.find_element_by_css_selector(".btn-lg.orange-btn").click()
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'domain-field')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
elem3 = driver.find_element_by_id("domain-field")
elem3.clear()
elem3.send_keys("sjtu.edu.cn")
elem3.send_keys(Keys.RETURN)
time.sleep(4)
personalElem = driver.find_element_by_xpath('//label[@for="personal-filter-field"]').click()
time.sleep(8)
while True:
    try:
        loadMoreButton=WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.show-more')))
        # loadMoreButton = driver.find_element_by_css_selector(".show-more").click()
        time.sleep(1)
        loadMoreButton.click()
        time.sleep(3)
    except Exception as e:
        print e
        break
print "Complete"
a=[];
a = driver.find_elements_by_class_name("email");
for i, item in enumerate(a):
    print a[i].text
time.sleep(10)

# pdb.set_trace()
# elem.send_keys(Keys.RETURN)
#
# driver.find_element_by_link_text("Sign in").click()

assert "No results found." not in driver.page_source

# driver.close()
