
import itertools
import urllib.request ,urllib.error
import re

def download(url):
    print('downloading:',url)
    try:
       html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error',e.reason)
        html = None

    return html



def crawl_sitemap(url):
    sitemap = download(url)
    print(sitemap.decode('utf-8'))
    links = re.findall('<loc>(.*?)</loc>',sitemap.decode('utf-8'))
    print(links)
    for link in links:
        html = download(link)
        pass


crawl_sitemap('http://example.webscraping.com/sitemap.xml')
