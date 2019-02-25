# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Xcw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.zgxiangcai.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_xcw(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_id("for_account").clear()
        driver.find_element_by_id("for_account").send_keys(u"小白")
        driver.find_element_by_name("pam_user[password]").clear()
        driver.find_element_by_name("pam_user[password]").send_keys("123456")
        driver.find_element_by_id("for_account").clear()
        driver.find_element_by_id("for_account").send_keys(u"小白擦")
        driver.find_element_by_id("for_account").clear()
        driver.find_element_by_id("for_account").send_keys(u"小白菜")
        driver.find_element_by_name("pam_user[pwd_confirm]").clear()
        driver.find_element_by_name("pam_user[pwd_confirm]").send_keys("123456")
        driver.find_element_by_id("for_mobile").clear()
        driver.find_element_by_id("for_mobile").send_keys("13120408386")
        driver.find_element_by_link_text(u"换一张").click()
        driver.find_element_by_id("iptlogin").clear()
        driver.find_element_by_id("iptlogin").send_keys("27se")
        driver.find_element_by_css_selector("span > span").click()
        driver.find_element_by_name("vcode").clear()
        driver.find_element_by_name("vcode").send_keys("416215")
        Select(driver.find_element_by_css_selector("select")).select_by_visible_text(u"北京市")
        driver.find_element_by_css_selector("option[value=\"110100\"]").click()
        Select(driver.find_element_by_xpath("//div[@id='area']/select[2]")).select_by_visible_text(u"昌平区")
        driver.find_element_by_id("format").click()
        Select(driver.find_element_by_id("format")).select_by_visible_text(u"个人")
        driver.find_element_by_id("for_license").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        Select(driver.find_element_by_id("size")).select_by_visible_text(u"100-299平")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_css_selector("span > span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=小白菜 | ]]
        driver.find_element_by_link_text(u"冰鲜虾").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=小白菜 | ]]
        driver.find_element_by_css_selector("img.imglazyload").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=小白菜 | ]]
        driver.find_element_by_xpath("//form[@id='items_action_form']/div/div[3]/div[2]/a/span/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=小白菜 | ]]
        driver.find_element_by_xpath("(//input[@id='ea'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='ea'])[2]").send_keys("12562@qq.com")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=小白菜 | ]]
        driver.find_element_by_xpath("//div[2]/div/div[3]/a/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=小白菜 | ]]
        self.assertEqual(u"确定要提交吗？", self.close_alert_and_get_its_text())
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
