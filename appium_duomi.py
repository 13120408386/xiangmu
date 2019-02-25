#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'Android Emulator'
#程序包名
desired_caps['appPackage'] = 'com.duomi.android'
# desired_caps['appPackage'] = 'com.android.bbkcalculator'
#程序启动类名
# desired_caps['appActivity'] = '.Calculator'
desired_caps['appActivity'] = '.DMLauncher'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
window_size=driver.get_window_size("current")
print(window_size)
#等待滑动界面的出现，因为只在到了这个界面他才有滑动的功能
s=driver.wait_activity('GuideActivity',10,2)
# 打印当前的activity
str=driver.current_activity
print(str)

# 宽 高
w=window_size["width"]
h=window_size["height"]
print(w,h)

# 滑动
index=0
while(index<3):
    driver.swipe(400, 400, 20, 400, 500);
    index+=1
    time.sleep(2)

#点击立即体验
try:
    driver.find_element_by_id('iv_start_weibo').click()
except :
    print("找不到控件")

time.sleep(4)
#竖向滚动
driver.swipe(200, 800*0.85, 200, 800*0.15, 500);
#重置应用
# driver.reset()

time.sleep(3)

contexts=driver.contexts

for c in contexts:
    print("context=",c)

cur=driver.current_context
print("current_context=",cur)

net_type=driver.network_connection

print("net_type=",net_type)

driver.quit()