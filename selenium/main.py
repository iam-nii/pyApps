# from selenium import webdriver
# from selenium.webdriver.common.by import By

# Keep the Chrome browser open after the program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# URL = "https://www.asos.com/the-north-face/the-north-face-himalayan-insulated-puffer-parka-coat-in-black" \
#       "/prd/205418853#colourWayId-205418856"
#
# driver.get(URL)
# price = driver.find_element(By.CLASS_NAME, value="MwTOW")
#
# print(f"The price is {price.text}")

# URL = "https://www.python.org/"
#
# bug_link_xpath = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
#
# driver.get(URL)
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute("placeholder"))
# bug_link = driver.find_element(By.XPATH, value=bug_link_xpath)
# print(bug_link.text)

############################  Exercise ##############################
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting up the chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

# Creating an instance of the web driver.
driver = webdriver.Chrome(options=chrome_options)
URL = "https://www.python.org/"
driver.get(URL)

anchor_paths = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a'
time_paths = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time'

upcoming_events_times = driver.find_elements(By.XPATH, value=time_paths)
upcoming_events_names = driver.find_elements(By.XPATH, value=anchor_paths)

times = [time.text for time in upcoming_events_times]
names = [name.text for name in upcoming_events_names]

# driver.close() # Closes the individual tab
driver.quit()  # Closes the whole browser

upcoming_events = {}

for count in range(len(times)):
    print(count)
    upcoming_events[f"{count}"] = {
                'time': f"{times[count]}",
                'name': f"{names[count]}"
            }

print(upcoming_events)

