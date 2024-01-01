from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://google.com")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search = driver.find_element(By.NAME, "q")

search.clear()
search.send_keys("Code with Mosh", Keys.ENTER)

# Wait for an element to exist
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Code with Mosh"))
)
result = driver.find_element(By.PARTIAL_LINK_TEXT, value="Code with Mosh")
result.click()

time.sleep(5)


driver.quit()

