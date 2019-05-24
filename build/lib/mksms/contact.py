class Contact(object):
    """This class represent a contact number. It is a convenience class.
    
    Args:
        * number: The number of the contact as str
        * name: The name of the contact as str
    """
    
    def __init__(self, number, name=""):
        self.number = number
        self.name = name
        
    def __str__(self):
        name = '"%s"'%self.name if self.name!=None else None
        return "{number:%s, name:%s}" % (self.number, name)
    
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