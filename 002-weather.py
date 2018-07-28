#! python3
#下载天气信息

import json, requests,sys,time

#输入参数：位置
if len(sys.argv)< 2:
    print("Usage:002-weather.py <your location>")
    sys.exit()

#将位置信息保存
location=' '.join(sys.argv[1:])

#访问sojson.com网站，获取天气信息
#接口使用说明
#每个IP日调用额度2000次，超过过多，我会直接封掉IP段。
#每次请求间隔必须3秒一次，如果多次超过3秒内调用多次，会封掉IP段
#IP解封，收费50元每次，单个IP永久不限制3秒也是50元，用来维护网站的开销。联系QQ：8446666【回答，天气接口解除限制】

url='https://www.sojson.com/open/api/weather/json.shtml?city=%s' % (location)
response = requests.get(url)
response.raise_for_status()

#将天气信息json保存至文件中
weatherData=json.loads(response.text)
w=weatherData['data']
print('Current weather in %s:' % (location))
print('Today:  %s  '  % (w['forecast'][0]['date']) ,' - 当前温度：  %s' % (w['wendu']))
print(w['forecast'][0]['high'], '  -  ', w['forecast'][0]['low'])
print()
print('Yesterday:  %s' %(w['yesterday']['date']))
print(w['yesterday']['high'], '  -  ', w['yesterday']['low'])

#间隔3秒
time.sleep(3)
