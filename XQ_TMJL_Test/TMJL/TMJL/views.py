# coding=utf-8

from django.http import HttpResponse

def tmjlTest(request):
    print(request)

    return HttpResponse("Hello world")


import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse



# 默认开启了csrf保护机制，本服务仅作自测使用，加上csrf_exempt去除掉csrf保护
@csrf_exempt
def index(request):

    print(request.environ)

    if request.method == 'POST':

        from django.core.handlers.wsgi import WSGIRequest

        print(request.POST)
        data = json.dumps(request.POST)
        print(data)
        try:
            header = data['header']
            payload = data['payload']
            print('header', 'payload')
            print(header, payload)
            if header['namespace'] == 'AliGenie.Iot.Device.Discovery':
                return discoverDevice(header,payload)
            if header['namespace'] == 'AliGenie.Iot.Device.Control':
                return controlDevice(header,payload)
        except:
            print('except')
            pass

        return HttpResponse('OK')



def discoverDevice(header,payload):

    response = {
        "header": {
            "namespace": "AliGenie.Iot.Device.Discovery",
            "name": "DiscoveryDevicesResponse",
            "messageId": "1bd5d003-31b9-476f-ad03-71d471922820",
            "payLoadVersion": 1
        },
        "payload": {
            "devices": [{
                "deviceId": "34ea34cf2e63",
                "deviceName": "灯泡",
                "deviceType": "light",
                "zone": "",
                "brand": "",
                "model": "",
                "icon": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1523179237874&di=9d8a8b60e514ade791db5021655fb4d0&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01114657b1cc6b0000012e7eac8a8b.jpg",
                "properties": [{
                    "name": "powerstate",
                    "value": "on"
                }],
                "actions": [
                    "TurnOn",
                    "TurnOff",
                ],
                "extensions": {
                    "extension1": "",
                    "extension2": ""
                }
            }]
        }
    }

    return HttpResponse(HttpResponse(json.dumps(response)), content_type='application/json')


def controlDevice(header,payload):

    response = {
        "header": {
            "namespace": "AliGenie.Iot.Device.Control",
            "name": "TurnOnResponse",
            "messageId": "1bd5d003-31b9-476f-ad03-71d471922820",
            "payLoadVersion": 1
        },
        "payload": {
            "deviceId": "34234"
        }
    }

    return HttpResponse(HttpResponse(json.dumps(response)), content_type='application/json')
