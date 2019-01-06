from selenium import webdriver;
from selenium.webdriver.common.keys import Keys

url = "https://www.facebook.com";
driver = webdriver.Chrome(executable_path="C:\\Users\\acer\\Desktop\\Drivers\\chromedriver.exe");
driver.get(url);

print(driver.title);

driver.close();