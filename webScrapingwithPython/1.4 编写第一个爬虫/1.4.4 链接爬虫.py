
import re
import urllib.request ,urllib.error


# 使用 urlparse 来使用相对链接
import urllib.parse

def download(url):
    print('downloading:',url)

    try:
       html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error',e.reason)
        html = None

    return html



def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)


def link_crawler(seed_url,link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url).decode('utf-8')

        for link in get_links(html):

            # check if link matches expected regex
            if re.match(link_regex,link):

                # from absolute link
                link = urllib.parse.urljoin(seed_url,link)
                print(link)

                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

    pass



link_crawler('http://example.webscraping.com','/(index|view)')



