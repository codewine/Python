
def login(self,posturl,postdata):
    '''
    self.build_opener()
    postdata = urllib.urlencode(postdata)
    request = urllib2.Request(url=posturl,data=postdata,headers=self.headers)
    #print self.opener.open(request)
    resp = urllib2.urlopen(request).read()
    print resp
    '''
    self.session = requests.Session()
    r = self.session.post(posturl,data=postdata,headers=self.headers)
    return dict(r.cookies) if not isinstance(r.cookies,dict) else r.cookies


def login_get_content(self,url,url_type='html'):
    content = self.session.get(url,timeout = 15)
    try:
        #get original data brfore transferring unicode
        content = content.content
    except UnicodeEncodeError:
        content = content.text.encode('utf-8')
    except UnicodeDecodeError:
        print 'test'
        content = content.text
    content = StringIO(content)
    #print content.read(),'test cstr'
    if url_type == 'json':
        return json.load(content)
    elif url_type == 'xml':
        return ET.parse(content)
    else:
        return BeautifulSoup(content,"html5lib")


class ZxSpider(CrawlSpider):
    name = 'zhixing'

    def start_requests(self):
        spider = Base_Spider('zhixing',['Host','Origin','Referer'])
        posturl = 'http://zhixing.bjtu.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
        postdata = {
            'username':'***',
            'password':'*****',
            'quickforward':'yes',
            'handlekey':'ls'
        }
        cookies = spider.login(posturl,postdata)

        url = 'http://zhixing.bjtu.edu.cn/thread-1047622-1-1.html'


        return [Request(url,cookies=cookies,callback=self.parse_page,headers=spider.headers)]

    def parse_page(self,response):
        sel = Selector(response)
        r = sel.xpath('//td[@id="postmessage_10415551"]/text()').extract_first()
        print r
        return r