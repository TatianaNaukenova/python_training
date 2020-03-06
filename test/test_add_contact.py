# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(Contact(firstname="Anna", lastname="Smith", mphone="+79111024402", email="qwerty@mail.mail", bday="1", bmonth="January", byear="1955"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(Contact(firstname="", lastname="", mphone="", email="", bday="", bmonth="-", byear=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


