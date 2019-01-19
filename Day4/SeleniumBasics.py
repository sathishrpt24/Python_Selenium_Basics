from selenium import webdriver;
from selenium.webdriver.support.ui import Select
import time as t

#url = "https://www.facebook.com";
url="C:\\Users\\acer\\Desktop\\firstHTML.html"

path = "C:\\Users\\acer\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path);

driver.get(url)\

    \;
test = driver.find_element_by_css_selector("#header7").text
print(test)
'''driver.find_element_by_name('firstname').send_keys("test")
driver.find_element_by_name('lastname').send_keys("user")
driver.find_element_by_name('reg_email__').send_keys("9876543210")
driver.find_element_by_name('reg_passwd__').send_keys("demo@123A")'''

day_Drop = driver.find_element_by_id("day")
month_drop = driver.find_element_by_id("month")

daySelect = Select(day_Drop).select_by_index(0)
print(daySelect)
monthSelect = Select(month_drop).select_by_value("8")
print(monthSelect)

#firstname:


print(driver.title);