import os
import sys
import unittest
from pprint import pprint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from mksms.contact import Contact
from mksms.message import Message, Response
from mksms.client import Client
import time


class ClientTestCase(unittest.TestCase):
    
    def test_a_send_message(self):
        contact = Contact("698368636", "fedim")
        message = Message(contact, "Salut molah")
        client = Client("830EA3BB2A", "73249341d85f566b6f2b8cef4563d6c149efe4df2b43f21776a6c9faf7f61af5")
        resp = client.send_message(message)
        self.assertEqual(resp.success, True)
        
    def test_b_start_verify(self):
        time.sleep(1)
        client = Client("830EA3BB2A", "73249341d85f566b6f2b8cef4563d6c149efe4df2b43f21776a6c9faf7f61af5")
        res = client.start_verify('677456798', 'MboateK')
        self.assertEqual(res.success, True)
        
    def test_c_confirm_verify(self):
        time.sleep(1)
        client = Client("830EA3BB2A", "73249341d85f566b6f2b8cef4563d6c149efe4df2b43f21776a6c9faf7f61af5")
        res = client.confirm_verify('677456798', '12345')
        self.assertEqual(res.success, True)
        
    def test_d_start_verify_fail(self):
        time.sleep(1)
        client = Client("830EA3BB2A", "73249341d85f566b6f2b8cef4563d6c149efe4df2b43f21776a6c9faf7f61af5")
        res = client.start_verify('677936798', 'MboateK')
        self.assertEqual(res.success, True)
        
    def test_e_confirm_verify_fail(self):
        time.sleep(1)
        client = Client("830EA3BB2A", "73249341d85f566b6f2b8cef4563d6c149efe4df2b43f21776a6c9faf7f61af5")
        res = client.confirm_verify('677456798', '76789')
        self.assertEqual(res.success, False)    
    
    def test_f_get_messages(self):
        client = Client("830EA3BB2A", "73249341d85f566b6f2b8cef4563d6c149efe4df2b43f21776a6c9faf7f61af5")
        msgs = client.get_messages()
        self.assertIsInstance(msgs, list)
        
    
if __name__ == "__main__":
    unittest.main()