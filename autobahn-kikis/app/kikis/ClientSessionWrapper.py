"""
==================================================================================

    ClientSessionWrapper.py 

    	ClientSession wrapper - calls RPC proceedures


==================================================================================
"""

from twisted.internet import reactor
from twisted.internet.error import ReactorNotRunning
from twisted.internet.defer import inlineCallbacks
from twisted.internet.defer import returnValue

from autobahn.twisted.util import sleep
from autobahn.wamp.types import RegisterOptions
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

from collections import OrderedDict

import sys

INPUT_ARRAY_SIZE = 16

class ClientSession(ApplicationSession):
    """
    Our WAMP session class .. place your app code here!
    """

    print("-----------------------------")
    print("Entered ClientSession CTOR - the wamp session class")
    print("-----------------------------")

    def onConnect(self):
        self.log.info("Local PY Client connected: {klass}", klass=ApplicationSession)
        self.join(self.config.realm, [u'anonymous'])
        print("OnConnect.....")

    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received", authmethod=challenge.method)
        print("OnChallenge.....")
        raise Exception("We haven't asked for authentication!")

    @inlineCallbacks
    def onJoin(self, details):

        self.log.info("Local PY Connected:  {details}", details=details)
        print("OnJoin.....")

        self._ident = details.authid
        self._type  = u'Python'

        self.log.info("Component ID is  {ident}", ident=self._ident)
        self.log.info("Component type is  {type}", type=self._type)

        #
        # extra is a dictionary with keys: 'nav_ld', and 'rpc_rl'
        # existing code will assert otherwise
        #



        extra=self.config.extra

        nav_ld = extra[u'nav_ld'] # navigation hops dictionary
        rpc_url  = extra[u'rpc_url']  # 'get' or 'set' instruction

        a = []
        for d in nav_ld:
            for key, value in d.items():
                a.append(key)
                a.append(value)
                #print('----------------------------')
                #print('key: ', key, ' value: ', value)
                #print('----------------------------')

        alen = len(a)
        #print('----------------------------')
        #print('length of a:', alen )
        #print('----------------------------')

        add_nulls = INPUT_ARRAY_SIZE - alen

        for x in range(add_nulls):
            a.append(u'NULL')
            #a.append(None)
        
 
        try:
            #res = yield self.call(u'com.kikis.get', 'wamp::Payload:', 1 )
            res = yield self.call(rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL' )

            print('----------------------------')
            print(' ClientSession::onJoin returns res =', res)
            print('----------------------------')

            self.config.extra[u'result'] = res

            self.disconnect()
            yield self.leave()
            self.disconnect()

           #----------
           # new attempt to restart event loop
           # import sys
           # del sys.modules['twisted.internet.reactor']
           # from twisted.internet import reactor
           # from twisted.internet import default
           # default.install()
           #----------

            #returnValue(res)
            return("got a value from server")

        except ApplicationError as e:
            ## ignore errors due to the frontend not yet having
            ## registered the procedure we would like to call
            if e.error != 'wamp.error.no_such_procedure':
                self.disconnect()
                raise e

    def onLeave(self, details):
        self.log.info("local py Router session closed ({details})", details=details)
        self.disconnect()

    def onDisconnect(self):
        self.log.info("Router connection closed")
        try:
            reactor.stop()
        except ReactorNotRunning:
            pass

        #----------
        # new attempt to restart event loop
        #import sys
        #del sys.modules['twisted.internet.reactor']
        #from twisted.internet import reactor
        #from twisted.internet import default
        #default.install()
        #----------


