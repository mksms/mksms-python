MKSms Client
===========

MKSms Client is a Python library written to handle/consume the MKSms API. Here is how to use::

    #!/usr/bin/env python

    from mksms.contact import Contact
    from mksms.message import Message, Response
    from mksms.client import Client

    contact = Contact("600000000", "Name")
    message = Message(contact, "Salut molah")
    client = Client("api_key", "api_hash")
    resp = client.send_message(message)
    self.assertEqual(resp.success, True)

