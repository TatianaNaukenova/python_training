from model.contact import Contact
from random import randrange


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="John", lastname="Smith"))
    old_contacts = app.contact.get_contact_list()
    # index = randrange(len(old_contacts))
    index = 1
    contact = Contact(mphone="999-999-999")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
