# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Jd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.jd.com/4bn"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_jd(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_id("key").clear()
        driver.find_element_by_id("key").send_keys(u"桔子")
        time.sleep(1)
        driver.find_element_by_css_selector("button.button").click()
        time.sleep(2)
        # 滚动
        js = "window.scrollTo(0,3000);"
        driver.execute_script(js)
        time.sleep(2)

        driver.find_element_by_css_selector(u"a[title=\"精选大个丑橘，现摘现发。新品上市，海南贵妃芒果，核薄肉多，领券减10元~新品上市，海南贵妃芒果，核薄肉多，领券减10元~\"] > img").click()
        # 窗口切换
        ck_list = driver.window_handles
        driver.switch_to.window(ck_list[1])
        time.sleep(2)

        driver.find_element_by_id("InitCartUrl").click()
        # driver.find_element_by_xpath("(//a[contains(@href, '//cart.jd.com/gate.action?pid=39037976098&pcount=1&ptype=1')])[3]").click()
    
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
