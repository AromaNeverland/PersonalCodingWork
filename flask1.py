import requests


def send_wechat(msg):
    token = 'XXXXXXXXXXXX'  # 前边复制到那个token
    title = 'title1'
    content = msg
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    print(url)
    r = requests.get(url=url)
    print(r.text)


if __name__ == '__main__':
    msg = 'Life is short I use python'
    send_wechat(msg)

/*{
    "appToken": "AT_xxx",
    "content": "Wxpusher祝你中秋节快乐!",
    "summary": "消息摘要", // 消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
    "contentType": 1, // 内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
  "topicIds": [ // 发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
                123
                ],
  "uids": [//发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
           "UID_xxxx"
           ],
  "url": "http://wxpusher.zjiecode.com" // 原文链接，可选参数
* /
