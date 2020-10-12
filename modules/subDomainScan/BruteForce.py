# -*- coding:utf-8 -*-
#@Time : 2020/4/15 16:52
#@Author: Triomphe
#@File : BruteForce.py

import DomainTransfer
from subDomainScan import header


def bf_subdomain(domain):
    result=[]
    response= header.header(domain)
    if response['Enable']:
        ip_list=DomainTransfer.domainTransfer(domain)
        result.append({'Server':response['Server'],'code':response['code'],'ip':ip_list,'domainname':domain})
    return  result

