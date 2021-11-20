 
import requests
 
Secret = "你自定义应用的 Secret"
corpid = '你注册的企业 corpid'
url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
 
getr = requests.get(url=url.format(corpid,Secret))
#
# print(r.json())
# {'errcode': 0, 'errmsg': 'ok', 'access_token': 't2HxARFMOgge-neHJwYXe4MrIXlFcu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg', 'expires_in': 7200}
 
access_token = getr.json().get('access_token')
 
# access_token ='t2HxARFMOgge-neHJwYXe4MrIXlFcu2m_Ev1pGQIAcmu-Kt1kQ7pey6jkPfdecqyvvZ9RGb3oSfjL1-lbbp1Y6UGGi8ZjNNd64AALtbR58ot1lh6VjE2ITkiWwgIftwWyryNDw_1AJAtVYYQxKU2O16a7NhHVEdcHG20u8czD-QUDUec1LqI4503OcVGzdR4Cq_4yA6a3fIkVLdQ_u3CHg'