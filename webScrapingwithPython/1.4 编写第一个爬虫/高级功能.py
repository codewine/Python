
# 解析robots.txt

import urllib.robotparser as robotparser
import urllib.request ,urllib.error , urllib.parse
import datetime ,time




rp = robotparser.RobotFileParser()
rp.set_url('http://example.webscarping.com/robots.txt')
rp.read()

url = 'http://example.webscraping.com'
user_agent = 'BadCrawler'
can = rp.can_fetch(user_agent,url)

print(can)


user_agent = 'GoodCrawler'
can = rp.can_fetch(user_agent,url)

print(can)




# 支持代理

def download(url,user_agent='wswp',proxy=None,num_retries=2):
    print('dowloading', url)

    headers = {'user-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)

    opener = urllib.request.build_opener()

    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))

    try:
        html = urllib.request.urlopen(request).read()
    except urllib.request.URLError as e:
        print('downloading error', e.reason)
        html = None

        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)

    return html



# 下载限速

class Throttle:
    '''
        add a delay between downloads for each domain
    '''

    def __init__(self,delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self,url):
        doamin = urllib.parse.urlparse(url).netloc
        last_accessed = self.domains.get(doamin)

        if self.delay > 0 and last_accessed is not None:

            sleep_sec = self.delay - (datetime.datetime.now() - last_accessed).seconds

            if sleep_sec > 0:
                time.sleep(sleep_sec)
            self.domains[doamin] = datetime.datetime.now()



#   避免爬虫陷阱
my_file = __import__("1.4.4 链接爬虫.py")


def link_crawler(seed_url,link_regex,max_depth=2):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    depth = seen[seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url).decode('utf-8')

        if depth != max_depth:
            for link in my_file.get_links(html):

                if link not in seen:

                    seen[link] = depth +1

                    crawl_queue.append(link)

    pass
