#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def getEarthapi(bot, contact, member):
    earthUrl = 'https://api.warframestat.us/pc/earthCycle'
    earthData = requests.get(earthUrl).json()
    print(earthData)
    if earthData['isDay']:
        earthString = '当前地球为:白天\n' + '剩余时间为:' + earthData['timeLeft']
    else:
        earthString = '当前地球为:黑夜\n' + '剩余时间为:' + earthData['timeLeft']
    bot.SendTo(contact, earthString)