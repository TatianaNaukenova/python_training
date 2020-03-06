from model.contact import Contact


def test_modify_contact_phone(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="John", lastname="Smith"))
    app.contact.modify_first_contact(Contact(mphone="999-999-999"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
