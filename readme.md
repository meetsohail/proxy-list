# Free Proxy List
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://github.com/Naereen/Strapdown.js/releases)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)



This library is for testing purpose while scraping.

## Installation
pip install free-proxy-list

## Usage
```python
from proxy_list import ProxyList
    
proxy_list = ProxyList()
```

### Get all Proxies?

#### Request	 
Call `get_all_proxies()` to get all the proxies in list form with their ports.

```python
proxy_list.get_all_proxies()
```

#### Response     
The response would be in form of multiple list of IP and Port.

```python
[('0.0.0.0','8080'),('0.0.0.0','9090'), and so on]
```

### Get Random Proxy?

#### Request	 
Call `get_random_proxy()` to get a single proxy to use directly in code.

```python
proxy_list.get_random_proxy()
```

#### Response     
The response would be in form of `dictionary` of IP and Port.

```python
{'https': '0:0:0.0:8080'}
```

### Get HTTPs Proxies?

#### Request

Call `get_https_proxies()` to get all the HTTPs proxies in list form with their ports.

#### Response
The response would be in form of multiple list of IP and Port.

```python
[('0.0.0.0','8080'),('0.0.0.0','9090'), and so on]
```


## How to use in requests?
Official documentation of requests. [Requests](https://docs.python-requests.org/en/master/)

```python
from proxy_list import ProxyList

proxies = ProxyList()
r = requests.get(url, proxies=proxies.get_random_proxy())
```