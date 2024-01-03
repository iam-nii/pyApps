import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FORM = 'https://forms.gle/TFGroLzP6a7c1yPG9'

ADDRESS_INPUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
PRICE_INPUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
LINK_INPUT = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

SUBMIT_BUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
SUBMIT_ANOTHER_RESPONSE = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'


class FillForm:
    def __init__(self, prices, links, addresses):
        # Settings
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.fill_fields(prices, links, addresses)

    def fill_fields(self, prices: list, links: list, addresses: list):
        self.driver.get(FORM)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ADDRESS_INPUT))
            )
        except Exception:
            print(Exception)
        else:
            for element in range(len(addresses)):
                time.sleep(2)
                # Fill the form
                address_input = self.driver.find_element(By.XPATH, ADDRESS_INPUT)
                price_input = self.driver.find_element(By.XPATH, PRICE_INPUT)
                link_input = self.driver.find_element(By.XPATH, LINK_INPUT)

                time.sleep(2)
                address_input.send_keys(addresses[element])
                print(addresses[element])
                price_input.send_keys(prices[element])
                print(prices[element])
                link_input.send_keys(links[element])
                print(links[element])

                # Submit the data
                submit = self.driver.find_element(By.XPATH, SUBMIT_BUTTON)
                submit.click()
                try:
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, SUBMIT_ANOTHER_RESPONSE))
                    )
                except Exception:
                    print(Exception)
                else:
                    time.sleep(2)
                    submit_another_response = self.driver.find_element(By.XPATH, SUBMIT_ANOTHER_RESPONSE)
                    submit_another_response.click()
        finally:
            self.driver.quit()


