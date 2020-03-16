from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, id=None,
                 homephone=None, mphone=None, email=None, workphone=None, fax=None, bday=None, bmonth=None, byear=None,
                 all_phones_from_homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mphone = mphone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



