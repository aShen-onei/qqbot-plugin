#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def getCetusapi(bot, contact, member):
    cetusUrl = 'https://api.warframestat.us/pc/cetusCycle'
    cetusData = requests.get(cetusUrl).json()
    print(cetusData)
    if cetusData['isDay']:
        cetusString = '平原现在还是白天哟（￣︶￣）\n\n' + 'BOSS还有' + cetusData['timeLeft'] + '才起床呢╰（￣▽￣）╭'
    else:
        cetusString = '平原现在是夜晚啦(#°Д°)\n\n' + '还有' + cetusData['timeLeft'] + '，勇敢的骚年快去战斗吧(ノ▼Д▼)ノ '
    bot.SendTo(contact, cetusString)