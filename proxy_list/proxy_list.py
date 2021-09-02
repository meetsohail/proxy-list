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
        return {'https:': (':'.join(choice(ip)))}

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


if __name__ == '__main__':
    proxy_list = ProxyList()
    print(proxy_list.get_all_proxies())
