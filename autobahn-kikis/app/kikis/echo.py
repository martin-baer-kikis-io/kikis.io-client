#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from __future__ import print_function

import os

from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver


class EchoClient(LineReceiver):
    end = b"Bye-bye!"

    def connectionMade(self):
        self.sendLine(b"Hello, world!")
        self.sendLine(b"What a fine day it is.")
        self.sendLine(self.end)


    def lineReceived(self, line):
        print("receive:", line)
        if line == self.end:
            self.transport.loseConnection()



class EchoClientFactory(ClientFactory):
    protocol = EchoClient

    def __init__(self):
        self.done = Deferred()


    def clientConnectionFailed(self, connector, reason):
        print('connection failed:', reason.getErrorMessage())
        self.done.errback(reason)


    def clientConnectionLost(self, connector, reason):
        print('connection lost:', reason.getErrorMessage())
        self.done.callback(None)



def main(reactor):

    url   = None
    realm = None

    rpc_url = u"com.kikis.get"
    url        = os.environ.get('CBURL', url )
    realm      = os.environ.get('CBREALM', realm )
    extra_dict = { rpc_url : a }

    print( ">>> realm:  ", realm)
    print( ">>> url:    ", url )

    factory = EchoClientFactory()
    reactor.connectTCP(url, rpc_url)
    return factory.done

if __name__ == '__main__':
    task.react(main)
