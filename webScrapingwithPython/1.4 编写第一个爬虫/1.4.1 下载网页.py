

# 互联网工程任务组 定义了http的错误完整列表
# https://tools.ietf.org/html/rfc7231#section-6



import urllib.request ,urllib.error

#
def download(url):
    print('downloading:',url)

    try:
       html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error',e.reason)
        html = None

    return html



# 5xx错误时重试

def download(url,num_retries=2):
    print('dowloading',url)

    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error', e.reason)
        html = None


        if num_retries >0:
            if hasattr(e,'code') and 500 <=e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url,num_retries-1)

    return html


# 设置用户代理 urllib2使用python-urllib/2.7 作为用户代理

# 设置用户代理

def dowmload(url,user_agent='wswp',num_retries=2):
    print('dowloading', url)

    headers = {'user-agent':user_agent}
    request = urllib.request.Request(url,headers=headers)
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