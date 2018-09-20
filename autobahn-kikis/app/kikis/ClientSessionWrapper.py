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


class ClientSession(ApplicationSession):
    """
    Our WAMP session class .. place your app code here!
    """

    def onConnect(self):
        self.log.info("Local PY Client connected: {klass}", klass=ApplicationSession)
        self.join(self.config.realm, [u'anonymous'])

    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received", authmethod=challenge.method)
        raise Exception("We haven't asked for authentication!")

    @inlineCallbacks
    def onJoin(self, details):


        self.log.info("Local PY Connected:  {details}", details=details)

        self._ident = details.authid
        self._type  = u'Python'

        self.log.info("Component ID is  {ident}", ident=self._ident)
        self.log.info("Component type is  {type}", type=self._type)

        # convert the navigation dict to the argument list
        extra=self.config.extra
       

        a = []
        for key in extra.keys():
            a.append(extra[key])

        l   = len(a)
        rem = 16 - l

        for i in range( rem  ):
            a.append(u'NULL')

        l   = len(a)

        try:
            #res = yield self.call(u'com.kikis.get', 'wamp::Payload:', 1 )
            res = yield self.call(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL' )

            print('----------------------------')
            print(' ClientSession::onJoin returns res =', res)
            print('----------------------------')

            self.config.extra[u'result'] = res

            reactor.stop()
            #returnValue(res)
            return("got a value from server")

        except ApplicationError as e:
            ## ignore errors due to the frontend not yet having
            ## registered the procedure we would like to call
            if e.error != 'wamp.error.no_such_procedure':
                reactor.stop()
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

