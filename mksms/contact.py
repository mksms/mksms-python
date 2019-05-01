class Contact(object):
    """This class represent a contact number. It is a convenience class."""
    
    def __init__(self, number, name=""):
        self.number = number
        self.name = name
        
    def __str__(self):
        return "{'number':%s, 'name':%s}" % (self.number, self.name)
    
    def to_dict(self):
        """Return the representation of the contact number like a dict"""
        return {'number':self.number, 'name':self.name}
    
    @staticmethod
    def from_dict(contact_dict):
        """Return a Contact instance from the dict passed"""
        if not isinstance(contact_dict, dict):
            raise ValueError("contact_dict must an instance of dict")
        number = contact_dict['number']
        name = contact_dict['name'] if 'name' in contact_dict else ''
        return Contact(number, name=name)