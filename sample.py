# -*- coding: utf-8 -*-

# 插件加载方法： 
# 先运行 qqbot ，启动成功后，在另一个命令行窗口输入： qq plug qqbot.plugins.sample
import earthApi
import cetusApi
import JSapi
import json

def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    elif '@ME' in content:
        if '地球' in content:
            earthApi.getEarthapi(bot, contact, member)
        if '平原' in content:
            cetusApi.getCetusapi(bot, contact, member)
        if '奸商' in content:
            JSapi.getJSapi(bot, contact, member)



