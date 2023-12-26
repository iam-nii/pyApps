import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
# Get the cookies
cookie = driver.find_element(By.ID, value="cookie")

# Get upgrade item ids
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# working with the clock
timeout = time.time() + 5
five_mins = time.time() + 60 * 5


while True:
    cookie.click()

    # Check every five seconds
    prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    item_prices = []

    for price in prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)


    # Create dictionary of store items and prices
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    # Getting the current cookie count
    money_element = driver.find_element(By.ID, value="money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)

    # Find the upgrades that we can currently afford
    affordable_upgrades = {}
    for cost,id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_upgrades[cost] = id

    # Purchase the most expensive affordable upgrade
    highest_affordable_upgrade = max(affordable_upgrades)
    print(highest_affordable_upgrade)
    purchase_item_id = affordable_upgrades[highest_affordable_upgrade]

    driver.find_element(By.ID, value=purchase_item_id).click()

    # Adding 5 more seconds until the next check
    timeout = time.time() + 5

    # After 5 mins, stop the bot and check the cookies per second count.
    if time.time() > five_mins:
        cookies_per_sec = driver.find_element(By.ID, value="cps").text
        print(cookies_per_sec)
        break
