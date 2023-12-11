import requests
import json
def callwx(email,wechat,want) :
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=707c57bf-abcd-4325-b7d6-c7dffcc54fb5" 

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"<font color=\"warning\">有新注册信息，请相关同事注意。</font>\n"
                       f">邮箱:<font color=\"comment\">  {email}</font>\n"
                       f">微信:<font color=\"comment\">  {wechat}</font>\n"
                       f">注册意愿:<font color=\"comment\">  {want}</font>\n"
        }
    }
    try:

        requests.post(url, headers=headers, data=json.dumps(data))

    except:
        print("err")