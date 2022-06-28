import requests
import config

urlAddress = config.test_url

class TestAPI:
    global urlAddress

    #控制台打印
    def _printResponse(self,response):
        print('\n\n---------- HTTP response * brgin ----------')
        print(response.status_code)

        for k,v in response.headers.item():
            print(f'{k}:{v}')
        print('')

        print(response.content.decode('utf8'))
        print('---------- HTTP response * end ----------\n\n')

    #百度接口
    def getBaidu(self):
        response = requests.get(url=urlAddress)

        return response

GetInfo = TestAPI()