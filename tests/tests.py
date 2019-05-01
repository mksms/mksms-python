import os
import sys
import unittest
from pprint import pprint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from mksms import Contact, Message, Response, Client


class ClientTestCase(unittest.TestCase):
    
    def test_a_send_message(self):
        contact = Contact("698368636", "fedim")
        message = Message(contact, "Salut molah")
        client = Client("82751BF244", "59d6b9e1e89de3d3aa4571c4ad45db8e971e79bf0b6c268cab66ed6cd0c9b07e")
        resp = client.send_message(message)
        pprint(resp.to_dict())
        self.assertEqual(resp.success, True)
        
    
if __name__ == "__main__":
    unittest.main()