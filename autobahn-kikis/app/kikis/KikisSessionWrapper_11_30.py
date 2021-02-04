"""
==================================================================================

    KikisSessionWrapper_11_30.py 

    	KikisSession wrapper - calls RPC proceedures


==================================================================================

"""

#import os
#import sys

#from twisted.internet import reactor
#from twisted.internet.error import ReactorNotRunning
#from twisted.internet.defer import inlineCallbacks
#from twisted.internet.defer import returnValue

##from autobahn.twisted.util import sleep
#from autobahn.wamp.types import RegisterOptions

#from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
#from autobahn.wamp.exception import ApplicationError

#INPUT_ARRAY_SIZE = 16



#---------------------------------------------------------------------------------=

    KikisSession class

#---------------------------------------------------------------------------------=

class KikisSession(ApplicationSession):

    def onConnect(self):

        print('>>> entered onConnect')
        self.log.info("Local PY Client connected: {klass}", klass=ApplicationSession)

        self.join(self.config.realm, [u'anonymous'])

        print('>>> leaving onConnect')

    @inlineCallbacks
    def onJoin(self, details):

        print('>>> entered onJoin')

        #
        # extra is dit that has the tree hops passed from client
        #
        extra=self.config.extra
        rpc_url  = next(iter(extra))

        a = extra[rpc_url] # navigation hop dictionary
        alen = len(a)
"""
        print('----------------------------')
        print('length of a:', alen )
        print('----------------------------')
"""

        add_nulls = INPUT_ARRAY_SIZE - alen
        for x in range(add_nulls):
            a.append(u'NULL')
            #a.append(None)
        
 
        try:
            res = 
                  yield self.call(rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], 
                                           a[6], a[7], a[8], a[9], a[10], a[11],
                                           a[12], a[13], a[14], a[15], u'NULL' )

            self.config.extra[u'result'] = res

            print('>>> leaving onJoin')
            self.leave()

            #return res

        except ApplicationError as e:
            ## ignore errors due to the frontend not yet having
            ## registered the procedure we would like to call
            if e.error != 'wamp.error.no_such_procedure':
                self.disconnect()
                raise e

    def onLeave(self, details):

        print('>>> entered onLeave')
        self.log.info("local py Router session closed ({details})", details=details)
        self.disconnect()
        print('>>> leaving onLeave')

    def onDisconnect(self):

        print('>>> entered onDisconnect')
        self.log.info("Router connection closed")
        print('>>> try block to stop reactor')
        try:
            print('>>> stop reactor')
            reactor.stop()
        except ReactorNotRunning:
            print('>>> reactor not running exception')
            pass


