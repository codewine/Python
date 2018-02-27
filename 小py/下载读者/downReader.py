# -*- coding: utf-8 -*-

import urllib.request
import os
from bs4 import BeautifulSoup




def urlBS(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    return soup

def main(url):
    soup = urlBS(url)
    link = soup.select('.booklist a')
    path = os.getcwd()+u'/读者文章保存'
    if not os.path.isdir(path):
        os.makedirs(path)

    for item in link:
        newurl = baseurl + item['href']
        result = urlBS(newurl)
        title = result.find("h1").string
        writer = result.find(id="pub_date").string.strip()
        filename = path + title + '.text'
        print(filename.encode("gbk"))
        new = open(filename ,"w")
        new.write("<<" + title.encode("gbk") + ">>\n\n")
        new.write(writer.encode("gbk")+"\n\n")
        text = result.select('.blkContainerSblkCon p')
        for p in text:
            context = p.text
            new.write(context.encode("gbk"))

        new.close()




if __name__ == '__main__':
    time = '2015_03'
    baseurl = 'http://www.52duzhe.com/' + time +'/'
    firsturl = baseurl + 'index.html'
    main(firsturl)