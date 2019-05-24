import requests
from datetime import datetime
from .contact import Contact
from .message import Message, Response

        
class Client(object):
    """This class a the client class for the API.
    
    Args:
        * api_key: Your api key
        * api_hash: Your api hash
    """
    
    ENDPOINT = {'send_sms':'/sms/send/',
                'get_sms':'/sms/available/',
                'start_verify':'/phone/verify/start/',
                'confirm_verify':'/phone/verify/confirm/'}
    
    BASE_URL = "http://api.mksms.cm"
    
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
    
    def get_messages(self, min_date=None, direction=Message.IN, read=False, 
                     timestamp=None):
        """This method is used to get the list of messages.
        
        Args:
            * min_date: datetime|str object representating the minimal date to use
            * direction: Union[BOTH|OUT|IN] the direction of the sms to return
            * read: False|True
            * timestamp: The minimum timestamp to fetch messages
            
        Return:
            * [Message, ...]
        """
        
        data = {'direction':direction, 'read':read, 'timestamp':timestamp}
        data['api_key'] = self.api_key
        data['api_hash'] = self.api_hash        
        if min_date:
            data['min_date'] = min_date
            
        endpoint = self.ENDPOINT['get_sms']
        res_req = self.session.get(self.BASE_URL+endpoint, params=data)
        res = res_req.json()
        
        messages = []
        for msg_dict in res:
            messages.append(Message.from_dict(msg_dict))
        return messages
    
    def start_verify(self, number, name):
        """THis method is used to start the number verification process.
        
        Args:
            * number
            
        Return:
            * Response object
        """
        
        assert isinstance(number, str)
        assert isinstance(name, str)
        
        data = {'number':number, 'name':name}
        data['api_key'] = self.api_key
        data['api_hash'] = self.api_hash
        
        endpoint = self.ENDPOINT['start_verify']
        res_req = self.session.post(self.BASE_URL+endpoint, json=data)
        res = res_req.json()
        
        return Response(res)
    
    def confirm_verify(self, number, code):
        """THis method is used to confirm the code for a started verification process
        
        Args:
            * number
            * code
            
        Return:
            * Response object
        """
        
        assert isinstance(number, str)
        assert isinstance(code, str)
        
        data = {'number':number, 'code':code}
        data['api_key'] = self.api_key
        data['api_hash'] = self.api_hash
        
        endpoint = self.ENDPOINT['confirm_verify']
        res_req = self.session.post(self.BASE_URL+endpoint, json=data)
        res = res_req.json()
        
        return Response(res)