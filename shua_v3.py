#env preparation
#pip install selenium splinter
#brew cask install chromedriver geckodriver

import random
def get_random_user_agent():
    #put any user_agents as we want
    user_agents=[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    ]
    return random.choice(user_agents)

from selenium import webdriver
from splinter import Browser
import re
pattern = '(\d+\.\d+\.\d+\.\d+)\s*(\d+)'

def get_all_proxies(page):
    #access the proxy_server page to get all protential proxies
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument("user-agent={ug}".format(ug=get_random_user_agent()))
    browser = Browser('chrome', options=chrome_options) #user_agent can monitor any device
    proxy_server_baseurl = "https://www.xicidaili.com/nn/{page}".format(page=page)
    browser.visit(proxy_server_baseurl)
    html = browser.find_by_id("ip_list").first.value
    proxy_list = []
    for ip in re.findall(pattern, html):
        proxy = ip[0] + ':' + ip[1]
        print("find potential proxy:", proxy)
        proxy_list.append(proxy)
    browser.quit()
    return proxy_list

import time
def shua_url_firefox(url, proxy, css_selector, delay):
    (host, port) = proxy.split(sep=":")
    print("try shua {url} using proxy:{host}:{port}".format(url=url, host=host, port=port)) 
    profile = {
        'network.proxy.http': host,
        'network.proxy.http_port': port,
        'network.proxy.ssl': host,
        'network.proxy.ssl_port': port,
        'network.proxy.type': 1,
        'network.http.altsvc.enabled': False
    }
    bs = Browser('firefox', profile_preferences=profile)
    bs.visit(url)
    bs.find_by_css(css_selector).first.click()
    time.sleep(delay)
    bs.quit()

input_definition = [
    {
        "url"          : "https://v.douyin.com/NsDs8T",
        "final_url"    : "https://www.iesdouyin.com/share/video/6643842692671343880/?region=NL&mid=6643842706210556675&u_code=16m0gmm2g&titleType=title&timestamp=1547668712&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy&iid=57944604896",
        "css_selector" : ".play-btn",
        "sleep"        : 12
    }
]

pages = list(range(1, 3555))
random.shuffle(pages)
for page in pages:
    proxy_list = get_all_proxies(page)
    if(len(proxy_list) == 0):
        continue
    for proxy in proxy_list:
        for item in input_definition:
            print("start to process:", item["url"]) 
            shua_url_firefox(item["final_url"], proxy, item["css_selector"], item["sleep"])
       
