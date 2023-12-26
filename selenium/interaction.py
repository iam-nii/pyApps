from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

URL = 'https://en.wikipedia.org/wiki/Main_Page'
driver.get(URL)

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

link = driver.find_element(By.LINK_TEXT, value="Ongoing")
link.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")

# driver.quit()