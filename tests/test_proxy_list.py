from proxy_list import ProxyList

proxy_list = ProxyList()


def test_get_random_proxy():
    proxy_list.get_random_proxy()


def test_get_all_proxies():
    proxy_list.get_all_proxies()


def test_get_https_proxies():
    proxy_list.get_https_proxies()