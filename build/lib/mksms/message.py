from .contact import Contact

class Message(object):
    """This class represent a message. It is a convenience class.
    
    Args:
        * contact: str|`Contact` the contact concerned by the sms
        * body: str the body of the sms
    """
    BOTH = 0
    OUT = 1
    IN = -1
    
    def __init__(self, contact, body, direction=OUT, read=False):
        if isinstance(contact, Contact):
            self.contact = contact
        elif isinstance(contact, str):
            self.contact = Contact(contact)
        else:
            raise ValueError("contact argument must be wether Contact or string instance")
        
        self.body = body
        self.direction = direction
        self.read = read
        
    def __str__(self):
        return "{body:\"%s\", contact:%s, direction:%s, read:%s}" % (self.body,
                            self.contact, self.direction, self.read)
    
    def to_dict(self):
        """Return the representation of the Message as a dict"""
        
        return {'contact':self.contact.to_dict(), 'body':self.body}
    
    @staticmethod
    def from_dict(msg_dict):
        """Return a Message instance from the dict passed"""
        
        if not isinstance(msg_dict, dict):
            raise ValueError("msg_dict must an instance of dict")
        return Message(Contact.from_dict(msg_dict['contact']),
                       msg_dict['body'], msg_dict['direction'],
                       msg_dict['read'])
    
    
class Response(object):
    """This class encapsulate a response of the API.
    
    Args:
        * res_dict: The dict of the response of the server
    """
    
    def __init__(self, res_dict):
        if not isinstance(res_dict, dict):
            raise ValueError("res_dict must an instance of dict")
        
        self.success = res_dict['success']
        if not self.success:
            self.message = res_dict['message']
        else:
            self.message = None
        self.data = res_dict
        
    def to_dict(self):
        """Return the underlined data as dict"""
        
        return self.data