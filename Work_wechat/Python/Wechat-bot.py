# -*- coding: utf8 -*-
import requests
Secret = "************--SM"   #你自定义应用的 Secret
corpid = '************'                            #你注册的企业 corpid
#获取access_token
url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
getr = requests.get(url=url.format(corpid,Secret))
access_token = getr.json().get('access_token')
#消息内容
data = {
   "touser" : "@all",   # 向这些用户账户发送
   "msgtype" : "text",
   "agentid" : ************,  # 应用的 id 号
   "text" : {
       "content" : "一看到你，我这张丑脸就泛起微笑^_^。"
   },
   "safe":0
}
import json
r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),
              data=json.dumps(data))

print(r.json())

def main_handler(event, context):     #防止云函数推送报错
   if __name__ == '__main__':
    main_handler()