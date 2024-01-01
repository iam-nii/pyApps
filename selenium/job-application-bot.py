import json
import html
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.xing.com/en"
MINIMUM_SALARY = 55

# Settings
chrome_extension = webdriver.ChromeOptions()
chrome_extension.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_extension)

driver.get(URL)

try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "consent-accept-button"))
    )
    driver.find_element(By.ID, "consent-accept-button").click()

except Exception:
    print(Exception)
else:
    # Job title
    search_job = driver.find_element(By.ID, "keywords-input")
    search_job.send_keys("full stack developer")

    # Applying for remote jobs
    remote_check = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/main/div/section[1]/div/div/div/div'
                                                 '/label[1]/span/input')
    remote_check.click()

#     Clicking the find jobs button
    find_jobs_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/main/div/section[1]/div/div/'
                                                  'form/button[2]')
    find_jobs_btn.click()

#     Waiting for the page to load
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lgkQbd"))
    )

#     Check if the job is full time, freelance or for students
    jobs_type = driver.find_elements(By.CSS_SELECTOR, "a > div > div > div > span > span")
    job_types = []
    salaries = []
    for pos in range(len(jobs_type)):
        if jobs_type[pos].text == "Full-time":
            job_types.append("Full-time")
            salaries.append(jobs_type[pos + 1].text)
        elif jobs_type[pos].text == "Freelance/Temp":
            job_types.append("Freelance/Temp")
            salaries.append("0")
        elif jobs_type[pos].text == "For students":
            job_types.append("For students")
            salaries.append("0")
        else:
            continue
    # print(job_types)
    # print(len(job_types))
    # print(salaries)
    # print(len(salaries))
    #     Finding the starting salary
    starting_sals = [salary.split(' ')[0].strip('€') for salary in salaries]
    # print(starting_sals)

#     Job link
    jobs_link = driver.find_elements(By.CSS_SELECTOR, "li > article > a ")
    job_links = [link.get_attribute("href") for link in jobs_link]
    # print(job_links)
    # print(len(job_links))

#   Job title
    jobs_title = driver.find_elements(By.CSS_SELECTOR, "li > article > a > div > div > div > div > h3")
    job_titles = [html.unescape(title.text) for title in jobs_title]
    # print(job_titles)
    # print(len(job_titles))

#     Dumping the data to a JSON file
    JOBS = {}
    for pos in range(len(job_titles)):
        JOBS[pos + 1] = {
            "Title": f"{job_titles[pos]}",
            "Type": f"{job_types[pos]}",
            "Starting salary": f"{starting_sals[pos]}",
            "Application link": f"{job_links[pos]}",
        }
    pprint.pprint(JOBS)

    try:
        # Check if the file exists and open it in read mode
        file = open("data.json", mode="r")
    except FileNotFoundError:
        # Catch exception if the file doesn't exist and create the file
        file = open("data.json", mode="w")
        json.dump(JOBS, file, indent=4)
        file.close()
    else:
        # If the file exists, update it
        all_jobs = json.load(file)
        file.close()
        all_jobs.update(JOBS)
        file = open("data.json", mode="r")
        json.dump(all_jobs, file)
        file.close()
finally:
    driver.quit()
    pass
