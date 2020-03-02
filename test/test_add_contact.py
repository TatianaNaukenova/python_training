# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="Anna", lastname="Smith", mphone="+79111024402", email="qwerty@mail.mail", bday="1", bmonth="January", byear="1955"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="", lastname="", mphone="", email="", bday="", bmonth="-", byear=""))
    app.session.logout()


