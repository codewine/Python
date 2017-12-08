
#   http://example.webscraping.com/view/Australia-2
#   使用ID代替国家名
#   http://example.webscraping.com/view/1


import itertools
import urllib.request ,urllib.error

def download(url):
    print('downloading:',url)

    try:
       html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error',e.reason)
        html = None

    return html



max_errors = 5
num_errors = 0


for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d'%page
    html = download(url)

    if html is None:

        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        # success -can scrape the result
        num_errors = 0
        pass