# -*- coding: UTF-8 -*-
from hello import *

app=Flask(__name__)

#加载出城市列表
city_list = load_list('city.list.json')

#得到所需城市温度并打印显示
temp_hefei = get_weather('Hefei', city_list)
print(temp_hefei)
temp_shanghai = get_weather('Shanghai', city_list)
print(temp_shanghai)
temp_nanjing = get_weather('Nanjing', city_list)
print(temp_nanjing)
temp_hangzhou = get_weather('Hangzhou', city_list)
print(temp_hangzhou)
temp_suzhou = get_weather('Suzhou', city_list)
print(temp_suzhou)

#以城市名为横坐标，温度值为纵坐标绘出散点图
names = ['Hefei','Shanghai','Nanjing','Hangzhou','Suzhou']
x = range(len(names))
y = [temp_hefei, temp_shanghai, temp_nanjing, temp_hangzhou, temp_suzhou]
plt.ylim(0, 30)
plt.scatter(x, y, alpha=0.6)
plt.xticks(x, names)
plt.savefig("static/image/temp_figure.png")
plt.show()

#调用函数，获取温度数值
temp_hefei_humid = get_weather_humid('Hefei', city_list)
print(temp_hefei_humid)
temp_shanghai_humid = get_weather_humid('Shanghai', city_list)
print(temp_shanghai_humid)
temp_nanjing_humid = get_weather_humid('Nanjing', city_list)
print(temp_nanjing_humid)
temp_hangzhou_humid = get_weather_humid('Hangzhou', city_list)
print(temp_hangzhou_humid)
temp_suzhou_humid = get_weather_humid('Suzhou', city_list)
print(temp_suzhou_humid)

#调用函数，获取湿度数值
names = ['Hefei','Shanghai','Nanjing','Hangzhou','Suzhou']
x = range(len(names))
y = [temp_hefei_humid, temp_shanghai_humid, temp_nanjing_humid, temp_hangzhou_humid, temp_suzhou_humid]
plt.ylim(0, 60)
plt.scatter(x, y, alpha=0.6)
plt.xticks(x, names)
plt.savefig("static/image/humid_figure.png")
plt.show()


@app.route('/')
def home():
    "该网页展示华东主要城市温度情况及湿度情况链接"
    return render_template('homepage.html')

@app.route('/humid/')
def humid():
    "相应湿度图"
    return render_template('humid.html')