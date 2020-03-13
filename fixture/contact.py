# from fixture.application import Application

from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creation_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def add_new(self, contact):
        driver = self.app.driver
        self.open_contact_creation_page()
        self.fill_contact_form(contact)
        # submit contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_text_field_value("firstname", contact.firstname)
        self.change_text_field_value("lastname", contact.lastname)
        self.change_text_field_value("mobile", contact.mphone)
        self.change_text_field_value("email", contact.email)
        self.change_calendar_value("bday", contact.bday)
        self.change_calendar_value("bmonth", contact.bmonth)
        self.change_text_field_value("byear", contact.byear)

    def change_calendar_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            Select(driver.find_element_by_name(field_name)).select_by_visible_text(text)
            driver.find_element_by_name(field_name).click()

    def change_text_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete__first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()
        # return to home page
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # init editing
        driver.find_elements_by_xpath("// img[@ alt='Edit']")[index].click()
        # driver.find_element_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit
        driver.find_element_by_xpath("//input[@value='Update']").click()
        self.app.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    # def edit_contact_by_index(self, index):
    #     driver = self.app.driver
    #     driver.find_element_by_xpath("//img[@alt='Edit']")[index].click()

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cache = []
            for element in driver.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)








