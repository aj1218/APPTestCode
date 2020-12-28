
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction  #鼠标操作
desired_caps = {}
#平台类型
desired_caps["platformName"] = "Android"
#平台版本号
desired_caps["platformVersion"] = "10"
#设备名称
desired_caps["deviceName"] = "Android Emulator"
#app包名  --安装 系统当中的标示
desired_caps["appPackage"] = "cn.nncz.nnapp"
#app入口 acitivty
#launchable-activity: name='com.zoontek.rnbootsplash.RNBootSplashActivity'
# label='' icon=''
desired_caps["appActivity"] = "com.zoontek.rnbootsplash.RNBootSplashActivity"
#重置与否
desired_caps["noReset"] = True

#连接我们的appium service 前提是 appium desktop要启动 ，有监听端口
#将desired_caps发给我们的appium server ，然后再去打开我们的app
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#运行代码之前，
#1：appium server 启动成功 处于监听状态；
#2：模拟器/真机必须等狗被电脑识别。即adb devices 能够识别到操作的
#id
# driver.find_element_by_id('com.lemon.lemonban:id/mavigation_tink')
# #class
# driver.find_element_by_class_name('android.wiget.FrameLayout')
# #content-decs
# driver.find_element_by_accessibility_id('')
#uiautomator java实现的
# driver.find_element_by_android_uiautomator('new Uiautomator().text("text名称")')
#点击属性1
WebDriverWait(driver,20).until(EC.invisibility_of_element_located((MobileBy.ID,"属性名1")))
driver.find_element_by_id('属性名1').click()
#点击属性2
WebDriverWait(driver,20).until(EC.invisibility_of_element_located((MobileBy.ID,"属性名2")))
driver.find_element_by_id('属性名2').click()
#appium 滑屏操作 滑动接口 swipe(起始)
size=driver.get_window_size()
start_X=size['width']*0.9
start_Y=size['height']*0.5

end_X=size['width']*0.1
end_Y=size['height']*0.5
#从右向左滑
driver.swipe(start_X,start_Y,end_X,end_Y,200)
#从左向右滑
driver.swipe(end_X,end_Y,start_X,start_Y,200)
#上下滑动
# 向上滑动 X轴不变，Y轴从大到小
driver.swipe(size['width']*0.5,size['height']*0.9,size['width']*0.5,size['height']*0.1)
# 向上滑动 X轴不变，Y轴从小到大
driver.swipe(size['width']*0.5,size['height']*0.1,size['width']*0.5,size['height']*0.9)

#鼠标操作












