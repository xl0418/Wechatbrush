#run below 2 command in your mac to setup env
#pip install selenium splinter
#brew cask install chromedriver
import random
def get_random_user_agent():
    #put any user_agents as we want
    user_agents=[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    return random.choice(user_agents)

from selenium import webdriver
from splinter import Browser
#access the proxy_server to get all protential proxies
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('lang=zh_CN.UTF-8')
chrome_options.add_argument("user-agent={ug}".format(ug=get_random_user_agent()))
browser = Browser('chrome', options=chrome_options) #user_agent can monitor any device
proxy_server_baseurl = "https://www.xicidaili.com/nn/{page}".format(page=random.randint(1,3555))
browser.visit(proxy_server_baseurl)

#parse all potential proxies
import re
pattern = '(\d+\.\d+\.\d+\.\d+)\s*(\d+)'
html = browser.find_by_id("ip_list").first.value
proxy_list = []
for ip in re.findall(pattern, html):
    proxy = ip[0] + ':' + ip[1]
    print("find potential proxy:", proxy)
    proxy_list.append(proxy)
browser.quit()

#now try to "shua" any url using above proxy
def shua_url_chrome(url, proxy):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument("user-agent={ug}".format(ug=get_random_user_agent()))
    options.add_argument('--proxy-server={proxy}'.format(proxy=proxy))
    #options.add_argument('--proxy-server=https://{proxy}'.format(proxy=proxy))
    print("try shua {url} using proxy:{proxy}".format(url=url, proxy=proxy))
    bs = Browser('chrome', options=options)
    bs.visit(url)
    #browser.find_by_id('kw').click() #如果需要点击播放
    bs.quit()

def shua_url_firefox(url, proxy):
    (host, port) = proxy.split(sep=":")
    profile = {
        'network.proxy.http': host,
        'network.proxy.http_port': port,
        'network.proxy.ssl': host,
        'network.proxy.ssl_port': port,
        'network.proxy.type': 1
    }
    print("try shua {url} using profile:{profile}".format(url=url, profile=profile))
    bs = Browser('firefox', profile_preferences=profile)
    bs.visit(url)
    #browser.find_by_id('kw').click() #如果需要点击播放
    bs.quit()

for proxy in proxy_list:
    shua_url_firefox("https://www.google.com", proxy)

