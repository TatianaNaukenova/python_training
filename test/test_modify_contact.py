from model.contact import Contact


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="John", lastname="Smith"))
    app.contact.modify_first_contact(Contact(mphone="999-999-999"))
