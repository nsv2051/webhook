# -*- coding: utf8 -*-
import requests

url = "你的api地址"

data = {
  "title":"ceshi",
  "description":"456",
  "url":"www.baidu.com",
  "header":"Content-type: application/x-www-form-urlencoded"
}

res = requests.post(url=url,data=data)

print(res.text)
