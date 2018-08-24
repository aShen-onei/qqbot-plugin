#!/usr/bin/python
# -*- coding: utf-8 -*-
# api测试
# https://api.warframestat.us/PC/earthCycle
# userheader = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
import urllib.request
import requests
import json
# def apitest():
#     earthurl = 'https://api.warframestat.us/pc/earthCycle'
#     response = requests.get(earthurl)
#     earthdata = response.json()
#     if earthdata['isDay']:
#         earthString='当前的地球为:白天\n'+'剩余时间为:'+earthdata['timeLeft']
#     else:
#         earthString='当前的地球为:夜晚\n'+'剩余时间为:'+earthdata['timeLeft']
#     return earthString
apiurl = 'https://api.warframestat.us/pc/sortie'
earthapi = 'https://api.warframestat.us/pc/earthCycle'
cetusapi = 'https://api.warframestat.us/pc/cetusCycle'
wmapi = 'https://api.warframe.market/v1/items/ash_prime_neuroptics/orders?include=item'
# response = urllib.request.urlopen(earthapi)
data = requests.get(earthapi)
# data = response.read()
earthdata = data.json()
if earthdata['isDay']:
    earthString = '当前的地球为:白天\n'+'剩余时间为:'+earthdata['timeLeft']
else:
    earthString = '当前的地球为:夜晚\n'+'剩余时间为:'+earthdata['timeLeft']

print(earthdata)
print(earthString)