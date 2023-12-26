from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")

first_name.send_keys("wonder")
last_name.send_keys("kid")
email.send_keys("wonderkid@youmail.com", Keys.ENTER)
# button.click()
