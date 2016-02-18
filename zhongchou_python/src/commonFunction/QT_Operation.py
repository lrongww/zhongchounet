# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
#公共功能模块的封装
import time

from WebDriverHelp import WebDriverHelp

class QT_Operations(object):
    
    def login(self,userName,passwd):
        WebDriverHelp().click_item("xpath", "/html/body/div[1]/div/div[1]/a[1]")
        
        WebDriverHelp().input_value("xpath","/html/body/div[21]/div/div[2]/form/div[1]/div[1]/input", userName)
        WebDriverHelp().input_value("xpath","/html/body/div[21]/div/div[2]/form/div[1]/div[2]/input", passwd)
        WebDriverHelp().click_item("id","login-btn")
        time.sleep(2)
        
    def logout(self):
        WebDriverHelp.geturl("http://www.zhongchou.cn/usernew-loginout")