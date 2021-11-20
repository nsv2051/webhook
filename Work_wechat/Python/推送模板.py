import requests
    message = res['message']
     if message == 'SUCCESS':
        print('自动签到成功')
        sendMessage('自动签到成功')
     else:
        print('自动签到失败，原因是：' + message)
        sendMessage('自动签到失败，原因是：' + message)
        # exit(-1)
# Qmsg酱通知
def sendMessage(msg):
    print('正在发送QQ通知。。。')
    res = requests.post(url='https://qmsg.zendee.cn/send/你的key?msg={0}'.format(str(msg)))
    code = res.json()['code']
    if code == 0:
        print('发送QQ通知成功。。。')
    else:
        print('发送QQ通知失败。。。')
        log(res.json())
        exit(-1)