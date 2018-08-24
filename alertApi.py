#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import re
import database
# def getAlertapi(bot, contact, member):
alertUrl = 'https://api.warframestat.us/pc/alerts'
alertData = requests.get(alertUrl).json()
alertString = ''
for alert in alertData:
    plantEn = re.findall(r'[^()]+', alert['mission']['node'])[1]
    plantZh = database.translatePlant(plantEn)
    plantExpression = re.compile(r'[(](.*?)[)]')
    plantOut = plantExpression.sub(plantZh, alert['mission']['node'])
    print(plantOut)
    missionTypeEn = alert['mission']['type']
    missionTypeZh = database.translateMissionType(missionTypeEn)
    print(missionTypeZh)
    rewardItem = alert['mission']['reward']['asString']
    rewardItem2 = rewardItem.split('+')
    print(rewardItem2[0])

print(alertString)
print(alertData)
