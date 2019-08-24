# WechatAutoWeather

# 通过微信公众测试号来定时给微信发送天气信息。
  （理论上开小号用itchat也可以做到，问题是我的小号不给登录网页版，看见酷安上的老哥用这个方式曲线救国，感觉还可以）

# 效果图
![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/1.jpg)

# 食用教程
  
  准备：
  云服务器一个，并且装有python3.x
  
  
# 首先注册公众测试号 ：https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
  
  将appID和appsecret填到代码里头
  ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/2.png)
  
  填写消息模板
  ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/4.png)

  扫码关注，然后将微信号填写在代码里头
   ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/3.png)
   
# 将填写好的代码扔到服务器上
  任意方法，我用的是WinScp传输到服务器
  
  python安装所需的库
  ```bash 
   pip install requests
  ```   
  
  后台运行代码
   ```bash 
   nohup python Main.py &
  ```   
  
