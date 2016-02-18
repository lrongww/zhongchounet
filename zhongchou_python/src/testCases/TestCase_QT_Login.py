# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
import unittest
import time

from commonFunction.WebDriverHelp import WebDriverHelp
from commonFunction.QT_Operation import QT_Operations
import sys 
sys.path.append("\commonFunction")

class testcases_login(unittest.TestCase):


    def setUp(self):
        #打开浏览器，并打开众筹网
        WebDriverHelp("open","firefox","local").geturl("http://www.zhongchou.com")
        time.sleep(2)


    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器


    def testlogin(self):
        #登录
        QT_Operations().login("18782952148", "zhongchou2015")
        #验证
        self.assertEqual(WebDriverHelp().get_text("css","a.siteHCountA.btn_ALink"),"用户QWY6214…")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()