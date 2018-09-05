# /usr/bin/python
# encoding:utf-8
import unittest
import time

from appium import webdriver
from ddt import ddt, data, unpack  # ddt包需要手动加载安装

""" Created by xiaoxiaojing on 2018/9/4 """


@ddt  # 测试类前加修饰，说明本测试类使用数据驱动框架
class MyTestCase(unittest.TestCase):
    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'A'
        desired_caps['appPackage'] = 'com.kimiss.gmmz.android'
        desired_caps['appActivity'] = '.ui.ActivityStart'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",
                                       desired_caps)

    # 当测试用例有多个参数时，使用元组存放被测数据
    @data(("jmetr", "123456", True),
          ("jmeter", "123456", False))
    @unpack  # 当测试用例有多个参数时使用，展开测试数据（告诉测试用例此时有多个参数）
    def test_login(self, username, password, expectresurlt):
        time.sleep(6)
        self.driver.find_element_by_id("iv_tab2_activity_main").click()
        time.sleep(1)
        self.driver.find_element_by_id("et_name_fragment_loain").send_keys(username)
        self.driver.find_element_by_id("et_pwd_fragment_login").send_keys(password)
        self.driver.find_element_by_id("btn_sub_fragment_login").click()
        try:
            if self.driver.find_element_by_id("btn_sub_fragment_login").is_displayed():
                exist = True
                print
                "loginfailed"
        except Exception as e:
            exist = False
            print("loginpass")
        self.assertEqual(exist, expectresurlt)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
