# -*- coding: UTF-8 -*-
import requests
import json
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template, session, redirect, url_for

app=Flask(__name__)

#我的API keys
api_keys = 'fe5edd43c2dbc4a330ee0e43bf9cece1'

#定义城市类
class City():
   def _init_(self, humidity, temperature):
       self.humidity = humidity
       self.temperature = temperature

#以json格式加载城市列表
def load_list(filename):
    f = io.open(filename,'r',encoding= 'utf-8')
    city_list = json.load(f)
    return city_list

#网站建议城市id查询，故创建该城市名与id间的转化函数
def search_city_id(city_name, city_list):
    for i in range(len(city_list)):
        if city_name==city_list[i]['name']:
            return city_list[i]['id']
    return False

#查询城市温度，并将开尔文转化为摄氏度
def get_weather(city_name, city_list):
    city_id = search_city_id(city_name, city_list)
    if city_id :
        city_weather = requests.get( 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&APPID='+api_keys)
        print('Status code', city_weather.status_code)
        response_dict = city_weather.json()
        # print(response_dict.keys())
        # print(city_weather.text)
        print(response_dict['main']['temp'])
        return (response_dict['main']['temp']-273.15)

#查询城市湿度
def get_weather_humid(city_name, city_list):
    city_id = search_city_id(city_name, city_list)
    if city_id :
        city_weather = requests.get( 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&APPID='+api_keys)
        print('Status code', city_weather.status_code)
        response_dict = city_weather.json()
        print(response_dict['main']['humidity'])
        return (response_dict['main']['humidity'])











