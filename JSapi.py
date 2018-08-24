#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def getJSapi(bot, contact, member):
    jsUrl = ' https://api.warframestat.us/pc/voidTrader'
    jsData = requests.get(jsUrl).json()
    print(jsData)
    if jsData['active']:
        jsString = '连接出现错误，请稍后再进行尝试'
    else:
        jsString = '奸商似乎还在来' + jsData['location'] + \
                   '的路上呢\n\n' + \
                   '预计时间到达时间' + jsData['startString'] + '后'
    bot.SendTo(contact, jsString)
