import requests
import json


base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
corpid = 'wwxxxxxxxxxx'  #企业ID
corpsecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Secret
agentid = 1000000  # 填写你的应用ID，不加引号，是个整型常数,就是上图的AgentId
usr = "@all"


def get_access_token():
    urls = base_url + 'corpid=' + corpid + '&corpsecret=' + corpsecret
    resp = requests.get(urls).json()
    access_token = resp['access_token']
    return access_token


def run(msg):
    data = {
        "touser": usr,
        "toparty": "@all",
        "totag": "@all",
        "msgtype": "text",
        "agentid": agentid,
        "text": {
            "content": msg
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    data = json.dumps(data)
    req_urls = req_url + get_access_token()
    resp = requests.post(url=req_urls, data=data).text
    print(resp)
    return resp




def main_handler(event,context):
    if event["httpMethod"] == "GET":
        text = event["queryString"]["text"]
    else:
        text = event["body"]
    run(text)


if __name__ == '__main__':
    run("")