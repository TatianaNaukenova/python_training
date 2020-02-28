# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_contact(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_contact_creation_page(driver)
        self.create_contact(driver, firstname="Anna", lastname="Smith", mob_phone="+79111024402", email="qwerty@mail.mail", bday="1", bmonth="January", byear="1955")
        self.return_to_homepage(driver)
        self.logout(driver)

    def test_add_empty_contact(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_contact_creation_page(driver)
        self.create_contact(driver, firstname="", lastname="", mob_phone="", email="", bday="", bmonth="-", byear="")
        self.return_to_homepage(driver)
        self.logout(driver)


    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, driver):
        driver.find_element_by_link_text("home page").click()

    def create_contact(self, driver, firstname, lastname, mob_phone, email, bday, bmonth, byear):
        # fill contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(firstname)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(lastname)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(mob_phone)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        # birthday
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(bday)
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(byear)
        # submit contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_creation_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, driver):
        driver.get("http://10.50.26.174/addressbook/edit.php")

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
