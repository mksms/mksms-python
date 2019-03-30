""""""
import requests
from datetime import datetime


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
    
    
class Message(object):
    """This class represent a message. It is a convenience class.
    Args:
        * contact: str|`Contact` the contact concerned by the sms
        * body: str the body of the sms
    """
    BOTH = 0
    OUT = 1
    IN = -1
    READ = 1
    UNREAD = -1    
    
    def __init__(self, contact, body, direction=OUT):
        if isinstance(contact, Contact):
            self.contact = contact
        elif isinstance(contact, str):
            self.contact = Contact(contact)
        else:
            raise ValueError("contact argument must be wether Contact or string instance")
        
        self.body = body
        self.direction = direction
        self.status = None
        
    def __str__(self):
        return "{body:%s, contact:%s, direction:%s, status:%s}" % (self.body,
                            self.contact, self.direction, self.status)
    
    def to_dict(self):
        """Return the representation of the Message as a dict"""
        return {'contact':self.contact, 'body':self.body}
    
    @staticmethod
    def from_dict(msg_dict):
        """Return a Message instance from the dict passed"""
        if not isinstance(msg_dict, dict):
            raise ValueError("msg_dict must an instance of dict")
        return Message(Contact.from_dict(msg_dict['contact']),
                       msg_dict['body'], msg_dict['direction'],
                       msg_dict['status'])
    
    
class Response(object):
    
    def __init__(self, res_dict):
        if not isinstance(res_dict, dict):
            raise ValueError("res_dict must an instance of dict")
        
        self.success = res_dict['success']
        if not self.success:
            self.message = res_dict['message']
        else:
            self.message = None
        
        
class Client(object):
    
    ENDPOINT = {'send_sms':'/sms/send/',
                'resend_sms':'/sms/resend/%s/',
                'get_sms':'/sms/'}
    BASE_URL = "http://mksms.mboatek.com"
    
    def __init__(self, api_key, api_hash):
        self.api_key = api_key
        self.api_hash = api_hash
        self.session = requests.Session()
        
    def send_message(self, message):
        """This methode is used send a message.
        Args:
            * message: Message object
        
        Return:
            * Response object
        """
        
        data = message.to_dict()
        data['api_key'] = self.api_key
        data['api_hash'] = self.api_hash
        endpoint = self.ENDPOINT['send_sms']
        res_req = self.session.post(self.BASE_URL+endpoint, json=data)
        res = Response(res_req.json())
        return res
    
    def get_messages(self, min_date=None, direction=OUT, status=UNREAD):
        """This method is used to get the list of messages.
        Args:
            * min_date: datetime|str object representating the minimal date to use
            * direction: Union[BOTH|OUT|IN] the direction of the sms to return
            * status: Union[READ|UNREAD|BOTH]
            
        Return:
            [Message, ...]
        """
        
        data = {'direction':direction, 'status':status}
        data['api_key'] = self.api_key
        data['api_hash'] = self.api_hash        
        if min_date:
            data['min_date'] = min_date
            
        endpoint = self.ENDPOINT['get_sms']
        res_req = self.session.get(self.BASE_URL+endpoint, data=data)
        res = res_req.json()
        
        messages = []
        for msg_dict in res:
            messages.append(Message.from_dict(msg_dict))
        return messages
        