from selenium import webdriver

import time 

import win32gui
import win32con
import win32clipboard as w
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口

def send(name, msg):

    #打开剪贴板
    w.OpenClipboard()
    #清空剪贴板
    w.EmptyClipboard()
    #设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    #获取剪贴板内容
    date = w.GetClipboardData()
    #关闭剪贴板
    w.CloseClipboard()
    #获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    #显示窗口
    win32gui.ShowWindow(handle,win32con.SW_SHOW)
    #把剪切板内容粘贴到qq窗口
    time.sleep(0.5)
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    #按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(1)#延缓进程


browser = webdriver.Chrome(executable_path ="D:\\chromedriver\\chromedriver.exe")

#2.通过浏览器向服务器发送URL请求
browser.get("http://ehall.whu.edu.cn/")
#  获取页面名为 wrapper 的 id 标签的文本内容
browser.find_element_by_xpath('//*[@id="username"]').send_keys('2020202130065')
browser.find_element_by_xpath('//*[@id="password"]').send_keys('051027')
browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]').click()
time.sleep(10)
browser.switch_to.window(browser.window_handles[0])
browser.get("http://yjs.whu.edu.cn//ssfw/navmenu.do?menuItemWid=0C33E50926E222A1E054001A4B090D2A&d=1614769136882")
browser.find_element_by_xpath('//*[@id="ryxxkTabButton"]/a').click()


while True:

	text = browser.find_element_by_xpath('//*[@id="ryxxkTable"]/tbody/tr[16]/td[9]/font').get_attribute('textContent')

	if text == "未满":
		print(time.strftime('%Y-%m-%d %H:%M:%S') + " 可以选课啦")
		send('流年、指尖的沙°',time.strftime('%Y-%m-%d %H:%M:%S') + " 可以选课啦")
		time.sleep(1)
		send('煭 火↣靑春',time.strftime('%Y-%m-%d %H:%M:%S') + " 可以选课啦")
		time.sleep(10)
		break
	elif text == "已满":
		print("已满")
		time.sleep(30)
		browser.refresh()
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="ryxxkTabButton"]/a').click()



