#!/usr/bin/python
# -- coding: utf-8 --
import sys
import datetime
import requests
import json
import time
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

# 设置循环时间，默认为8个钟
second = sleeptime(8,0,0);

def get_access_token():
    """
    获取微信全局接口的凭证(默认有效期俩个小时)
    如果不每天请求次数过多, 通过设置缓存即可
    """
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": "填写你微信测试号的Appid",
            "secret": "填写你微信测试号的appsecret",
        }
    ).json()
    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token


def sendmsg(openid,msg,access_token,templateId):

    body = {
        "touser": openid,
        "template_id":templateId,
        # "6S39Gv7rcdD4xIijbBF0NPvmtywdxja7lrrMfMLAQH8",
        "url":"www.caiyunapp.com/map",
        "data": {
            "weather":{
                "value": msg,
                "color":"#173177"
            }
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="+access_token,
        data=bytes(json.dumps(body,ensure_ascii=False).encode("utf-8"))
    )
    result = response.json()
    print(result)

def getmsg(city,jwd):
    json_text = requests.get(str.format(jwd)).content
    self_realtime_data = json.loads(json_text)
    status=self_realtime_data['status']
    json_text=requests.get(str.format(city)).content
    data = json.loads(json_text)
    cityid=data['cityid']
    city=data['city']
    date=data['date']
    utime=data['update_time']
    week=data['week']
    wea=data['wea']
    h_tem=data['tem1']
    l_tem=data['tem2']
    n_tem=data['tem']
    win=data['win']
    win_speed=data['win_speed']
    win_meter=data['win_meter']
    hum=data['humidity']
    visit=data['visibility']
    pressure=data['pressure']
    air=data['air']
    pm25=data['air_pm25']
    air_level=data['air_level']
    air_tips=data['air_tips']
    alarm=data['alarm']['alarm_content']
    alarm_type=data['alarm']['alarm_type']
    alarm_level=data['alarm']['alarm_level']
    if status=='failed':
        send_data=city+"天气预报：\n"+"\n天气："+wea+"  "+n_tem+"℃\n最高/低温："+h_tem+"℃ /"+l_tem+"℃\n湿度："+hum+"\n"+win+"  "+win_speed+"  "+win_meter+"\n能见度："+visit+"\n空气质量："+air+"  "+air_level+"  "+air_tips+"\npm2.5："+pm25+"\n预警消息："+alarm+"\n更新时间："+date+" "+week+" "+utime+"\n数据来源：中国天气网\n当您看到这条消息时，彩云天气api已经到达配额上限，请点击详情手动查询降雨预报"
    else:
        now_data=self_realtime_data['result']['forecast_keypoint']
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        send_data="降雨预报：\n"+now_data+"\n更新于："+nowTime+"\n天气："+wea+"  "+n_tem+"℃\n最高/低温："+h_tem+"℃ /"+l_tem+"℃\n湿度："+hum+"\n"+win+"  "+win_speed+"  "+win_meter+"\n能见度："+visit+"\n空气质量："+air+"  "+air_level+"  "+air_tips+"\npm2.5："+pm25+"\n预警消息："+alarm+"\n"
    return send_data


if __name__ == '__main__':
    while(True):
        access_token = get_access_token()
        # sendmsg函数可以复制多个，每个都填写不同的信息，就可以做到同时给多个微信号发送了。
        sendmsg('测试号上的微信号',
                getmsg("https://www.tianqiapi.com/api/?version=v6&city=城市名",
                "https://api.caiyunapp.com/v2/你的彩云天气APPtoken/经纬度/minutely.json"),
                access_token,"模板号")

        time.sleep(second)

