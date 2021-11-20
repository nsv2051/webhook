### bot-1
图片推送:https://bot.*********.workers.dev/bot1650965042:******/sendPhoto?chat_id=14*****4989&&photo=https://******.jpg

文本推送:https://bot.*********.workers.dev/bot1650965042:******/sendMessage?chat_id=*****989&text=123
***
### sendMessage（直接文本，支持MarkdownV2/HTML）

https://api.telegram.org/bot1545138812:AAGroid6uSJFbQxRM2f8X6KHlsnDReHUkvE/sendMessage?chat_id=1138220708&text=Hi,MJJ

### sendPhoto(单张图片。最大10M，可以url地址或者本地图片)

https://api.telegram.org/bot1545138812:AAGroid6uSJFbQxRM2f8X6KHlsnDReHUkvE/sendPhoto?chat_id=1138220708&photo=https://pixiv50.com/static/images/wcldpgn/6203904_82693450_p0.jpg

### sendVideo（最大50M，只支持mp4） 加标题参数 caption

https://api.telegram.org/bot1545138812:AAGroid6uSJFbQxRM2f8X6KHlsnDReHUkvE/sendVideo?chat_id=1138220708&video=https://cdntube2.b-cdn.net/mp4/6ce773dc977f726cd5d56cb28d9d77b2414a6497.mp4&caption=Laura's got big tittie's

### 加 标题参数 caption， 格式参数parse_mode ，用MarkdownV2模式给标题加超链接

https://api.telegram.org/bot1545138812:AAGroid6uSJFbQxRM2f8X6KHlsnDReHUkvE/sendVideo?chat_id=1138220708&video=https://cdntube2.b-cdn.net/mp4/6ce773dc977f726cd5d56cb28d9d77b2414a6497.mp4&caption=[Laura's got big tittie's](https://4k5.net/read-8127.html)&parse_mode=MarkdownV2

### sendMediaGroup（多个媒体，一次最多好像9个，以json模式，第一张图加标题参数）

https://api.telegram.org/bot1545138812:AAGroid6uSJFbQxRM2f8X6KHlsnDReHUkvE/sendMediaGroup?chat_id=1138220708&media=[{"caption":"[Pixiv50](https://pixiv50.com/)","parse_mode":"MarkdownV2","type":"photo","media":"https://pixiv50.com/static/images/wcldpgn/6203904_82693450_p0.jpg"},{"type":"photo","media":"https://www.pixiv50.com/static/images/iamcnqu/3371956_83774670_p0.jpg"}]