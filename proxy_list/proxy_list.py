import requests
from bs4 import BeautifulSoup
from random import choice


class ProxyList:

    def __init__(self, url='https://free-proxy-list.net'):
        self.url = url

    def get_random_proxy(self):
        table = self.scrape_list()
        ip = (list(zip(map(lambda td: td.text, table.findAll(
            "td")[::8]), map(lambda td: td.text, table.findAll("td")[1::8]))))
        return {'https': (':'.join(choice(ip)))}

    def get_all_proxies(self):
        table = self.scrape_list()
        ips = list(zip(map(lambda td: td.text, table.findAll(
            "td")[::8]), map(lambda td: td.text, table.findAll("td")[1::8])))
        return ips

    def scrape_list(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.findAll('table')[0]
        return table

    def get_https_proxies(self):
        ips = []
        table = self.scrape_list()
        all_proxies = list(zip(map(lambda td: td.text, table.findAll(
            "td")[::8]), map(lambda td: td.text, table.findAll(
                "td")[1::8]), map(lambda td: td.text == 'yes', table.findAll("td")[6::8])))
        for ip, port, https in all_proxies:
            if https == True:
                ips.append((ip, port))
        return ips