# WechatAutoWeather

# 通过微信公众测试号来定时给微信发送天气信息。
  （理论上开小号用itchat也可以做到，问题是我的小号不给登录网页版，看见酷安上的老哥用这个方式曲线救国，感觉还可以）
  <br>
# 效果图
![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/1.jpg)

# 食用教程
  
### 准备：
  1.云服务器一个，并且装有python3.x
  <br>
  2.彩云天气开发者账户（https://open.caiyunapp.com/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94_API），自行申请就OK
  
### 首先注册公众测试号 ：https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
  <br>
  <br>
  <br>
  <br>
  
### 将appID和appsecret填到代码里头
  ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/2.png)
  <br>
  <br>
  <br>
  <br>
  
  
### 填写消息模板
  ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/4.png)

  <br>
  <br>
  <br>
  <br>
  
###  扫码关注，然后将微信号填写在代码里头
  ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/3.png)
  
  <br>
  <br>
  <br>
  <br>
 
### 再把代码里我中文标注的地方填完就OK（例如彩云科技API），准备最后一步 
  ![Image text](https://github.com/6yi/WechatAutoWeather/blob/master/Demoimg/5.png)
  <br>
#### 图中的经纬度需要你自己查询（http://www.gpsspg.com/maps.htm） 经度在前，纬度在后，例：114.00,23.34 
  <br>
  <br>
  <br>
  <br>  
 
# 将填写好的代码扔到服务器上
### 任意方法，我用的是WinScp传输到服务器
  
  python安装所需的库
  ```bash 
   pip install requests
  ```   
  
  后台运行代码
   ```bash 
   nohup python Main.py &
  ```   
  
