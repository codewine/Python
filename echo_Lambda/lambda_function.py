import requests
import json

def lambda_handler(event, context):

    access_token = event['payload']['accessToken']

    if event['header']['namespace'] == 'Alexa.ConnectedHome.Discovery':

        return handleDiscovery(context, event)

    elif event['header']['namespace'] == 'Alexa.ConnectedHome.Control':

        return handleControl(context, event)


def handleDiscovery(context, event):
    payload = ''

    header = {

        "namespace": "Alexa.ConnectedHome.Discovery",
        "name": "DiscoverAppliancesResponse",
        "payloadVersion": "2"
        }

    if event['header']['name'] == 'DiscoverAppliancesRequest':
        payload = {

            "discoveredAppliances":[

                {
                    "applianceId":"device001",
                    "manufacturerName":"lawTest",
                    "modelName":"lamp",
                    "version":"1.1",
                    "friendlyName":"Smart Home Virtual Device",
                    "friendlyDescription":"Virtual Device for the Sample Hello World Skill",
                    "isReachable":True,
                    "actions":[
                        "turnOn",
                        "turnOff"
                    ],

                    "additionalApplianceDetails":{

                        "extraDetail1":"optionalDetailForSkillAdapterToReferenceThisDevice",

                        "extraDetail2":"There can be multiple entries",

                        "extraDetail3":"but they should only be used for reference purposes.",

                        "extraDetail4":"This is not a suitable place to maintain current device state"

                    }

                }

            ]

        }

    return {'header': header, 'payload': payload}



def ControlTest(context, event):

    print(context)
    payload = ''
    url = 'https://corp.xqopen.cn/comen/v1/devices/B28428483617095680/ctrl'
    values = {' contextId':'',
                'msg':'83f2addc521ae734201e77072f301e3d7045a3a087de17cf5b6c173ab901d8495bd1bb1c54ab388c6b429e86e3a0cb27'
             }
    data = json.dumps(values)
    print (data)
    headers = {'Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9',
                'Content-Type':'application/json',
                'User-Agent':'comen/1.0.1706210 (iPhone; iOS 10.3.2; Scale/2.00)',
                'language':'zh-CN',
                'token':'TOKEN20171121121950RIf1Oyc4J',
                'userId':'B28425351294091264',
                'serviceId':'interunion',
                'accept-language':'zh-CN',
                }


    req = requests.post(url,data,headers=headers)
    the_page = req.text
    print(the_page)

    return the_page

