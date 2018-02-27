import requests


def re_demo():
    response = requests.get("https://www.baidu.com")
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)
    print(response.content)
    print(response.content.decode("utf-8"))

# 各种请求方式
def re_method():
    requests.post("http://httpbin.org/post")
    requests.put("http://httpbin.org/put")
    requests.delete("http://httpbin.org/delete")
    requests.head("http://httpbin.org/get")
    requests.options("http://httpbin.org/get")

#get 带上头部信息
def get_headers():
    heardrs = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }
    response = requests.get("https://www.zhihu.com", headers=heardrs)
    print(response.text)

# get 请求带参数
def get_params():
    data = {
        "name": "zhaofan",
        "age": 22
    }
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.url)
    print(response.text)



# 基本POST请求
def post_normal():
    data = {
        "name": "zhaofan",
        "age": 23
    }
    response = requests.post("http://httpbin.org/post", data=data)
    print(response.text)


# request的参数
def post_re():
    response = requests.get("http://www.baidu.com")
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.url), response.url)
    print(type(response.history), response.history)


# 测试是否访问成功
def test_success():
    response = requests.get("http://www.baidu.com")
    if response.status_code == requests.codes.ok:
        print("访问成功")



# request的文件上传
def upload_file():

    files = {"files":open("418.jpg",mode="rb")}
    response = requests.post("http://httpbin.org/post", files=files)
    print(response.text)



# 获取cookie
def get_cookie():
    response = requests.get("http://www.baidu.com")
    print(response.cookies)

    for key, value in response.cookies.items():
        print(key + "=" + value)


# 会话维持
def keep_cookie():
    s = requests.Session()
    s.get("http://httpbin.org/cookies/set/number/123456")
    response = s.get("http://httpbin.org/cookies")
    print(response.text)


# 证书验证
def use_certification():
    import requests
    from requests.packages import urllib3
    urllib3.disable_warnings()
    response = requests.get("https://www.12306.cn", verify=False)
    print(response.status_code)

    # 也可以通过cert参数放入证书路径



# 代理设置
def use_profixy():
    proxies = {
        "http": "http://127.0.0.1:9999",
        "https": "http://127.0.0.1:8888"
    }
    response = requests.get("https://www.baidu.com", proxies=proxies)
    print(response.text)

    '''
    如果代理需要设置账户名和密码, 只需要将字典更改为如下：
    proxies = {
        "http": "http://user:password@127.0.0.1:9999"
    }
    如果你的代理是通过sokces这种方式则需要pip install "requests[socks]"
    proxies = {
        "http": "socks5://127.0.0.1:9999",
        "https": "sockes5://127.0.0.1:8888"
    }

    '''

# 超时设置
def re_timout():
    response = requests.get("http://www.baidu.com", timeout=2)
    # response = requests.get('http://github.com', timeout=2)
    print(response.text)

    ''' 通过timeout参数可以设置超时的时间 '''


# 认证设置
def re_auth():
    from requests.auth import HTTPBasicAuth
    response = requests.get("http://120.27.34.24:9001/", auth=HTTPBasicAuth("user", "123"))
    print(response.status_code)

# 异常处理
def re_expection():
    from requests.exceptions import ReadTimeout, ConnectionError, RequestException
    try:
        response = requests.get("http://httpbin.org/get", timout=0.1)
        print(response.status_code)
    except ReadTimeout:
        print("timeout")
    except ConnectionError:
        print("connection Error")
    except RequestException:
        print("error")



re_timout()