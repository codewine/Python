import requests

heardrs = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
response = requests.get("http://www.eyepetizer.net/detail.html?vid=5560", headers=heardrs)
print(response.content.decode("utf-8"))
