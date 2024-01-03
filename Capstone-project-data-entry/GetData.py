import pprint

from bs4 import BeautifulSoup
import requests
from SendData import FillForm

class GetData:
    def __init__(self):
        """A class that grabs data from a property listing website and sends
        the data to another class for storage"""

        self.response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
        self.content = self.response.text

        self.soup = BeautifulSoup(self.content, 'html.parser')
        self.prices = self.get_prices()
        self.addresses = self.get_addresses()
        self.links = self.get_links()
        self.send_data = FillForm(prices=self.prices, links=self.links, addresses=self.addresses)

    def get_prices(self):
        prices = self.soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
        prices_list = [price.getText().split('/')[0].split('+')[0] for price in prices]
        # print(prices_list)
        return prices_list

    def get_addresses(self):
        addresses = self.soup.select(selector="address")
        addresses_list = [address.getText().strip('\n').strip() for address in addresses]
        # pprint.pprint(addresses_list)
        return addresses_list

    def get_links(self):
        links = self.soup.select(selector='article > div > div > a')
        links_list = [link.get('href') for link in links]
        # pprint.pprint(links_list)
        return links_list