# -*- coding: utf-8 -*-
"""
Test qpid 

Since the passwords have to go in a URL - make sure you 'encode' them.... 
stupid hashes....


pip install python-qpid-proton

"""
import urllib
import glob
import logging
import time
import uuid

from proton import Message
from proton.utils import BlockingConnection

servername="test.wencomine.sydney.gacims.net"
serverport=5672
creds=("wencoservices", urllib.parse.quote_plus('*****CHANGEME******'))

messagePattern="*.xml"
myFileList = glob.glob(messagePattern, recursive=False)



logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


conn = BlockingConnection(url="amqp://{}:{}@{}:{}/".format(creds[0],creds[1],servername, serverport))
sender = conn.create_sender("FMS.Outbound.WorkExecuted")

for file in myFileList:
    with open(file) as f:
        myMessage = Message(body=f.read(), 
                            annotations={"one":1, "two":2}, 
                            creation_time=time.time(), 
                            id=uuid.uuid1(), 
                            correlation_id=uuid.uuid1(),
                            subject=file)

    sender.send(myMessage, timeout=10);
    logger.info("sent message: {}".format(file))

conn.close()