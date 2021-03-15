# -*- coding: utf-8 -*-
# @Time    : 2021/3/15
# @Author  : lxdebug
# @Email   : lxdebug@foxmail.com

import requests
import platform
import json

#正则表达式


def getnetinfo(): 
    netinfo = requests.get('http://ip-api.com/json/').text
    ip = json.loads(ipinfo).get('query')
    country = json.loads(ipinfo).get('country')
    return ip,country

def system():
    if(platform.system()=='Windows'):
        return 'windows'
    elif(platform.system()=='Linux'):
        return 'linux'
    else:
        return 'other'

   