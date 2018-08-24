#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

def translatePlant(plant):
    file = open('D:\迅雷下载\WFA_Lexicon-master (1)\WFA_Lexicon-master\WF_Dict.json', encoding='UTF-8');
    data = json.load(file);
    for index in data:
        if (index['En'] == plant):
            plant = index['Zh']
    return plant
def translateMissionType(Type):
    file = open('D:\迅雷下载\WFA_Lexicon-master (1)\WFA_Lexicon-master\WF_Dict.json', encoding='UTF-8');
    data = json.load(file);
    for index in data:
        if(index['En'] == Type):
            Type = index['Zh']
    return Type
def translateAlertreward(reward):
    file = open('D:\迅雷下载\WFA_Lexicon-master (1)\WFA_Lexicon-master\WF_Alert.json', encoding='UTF-8');
    data = json.load(file);

