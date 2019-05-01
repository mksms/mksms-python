""""""
import requests
from datetime import datetime
from .contact import Contact
from .message import Message, Response
from pprint import pprint

        
class Client(object):
    
    ENDPOINT = {'send_sms':'/sms/send/',
                'resend_sms':'/sms/resend/%s/',
                'get_sms':'/sms/'}
    BASE_URL = "http://api.mksms.cm:8000"
    
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
        pprint(data)
        data['api_key'] = self.api_key
        data['api_hash'] = self.api_hash
        endpoint = self.ENDPOINT['send_sms']
        res_req = self.session.post(self.BASE_URL+endpoint, json=data)
        res = Response(res_req.json())
        return res
    
    def get_messages(self, min_date=None, direction=Message.OUT, status=Message.UNREAD):
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
        