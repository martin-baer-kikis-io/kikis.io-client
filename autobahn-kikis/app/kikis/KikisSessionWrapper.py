#
#    KikisSessionWrapper.py 
#
#       calls remote procedures on Windows host
#

#-----------------------------------------------------------------------

import os
import sys

# simple debug logging
import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

#from functools import wraps

from autobahn.wamp.exception import ApplicationError
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

import twisted.internet.defer 
from twisted.internet import reactor, defer
from twisted.internet.defer import ensureDeferred, inlineCallbacks, returnValue
from twisted.internet.error import ReactorNotRunning

#-----------------------------------------------------------------------

class KikisSession(ApplicationSession):

    # kikis session class 

    def onConnect(self):

        log.debug('onConnect--------------------------------------------------')

        self.log.info("Local PY Client connected: {klass}", klass=ApplicationSession)
        #log.debug("Local PY Client connected: {klass}", klass=ApplicationSession)
        self.join(self.config.realm, [u'anonymous'])

        log.debug('onConnect----------------------------------------------')

    #-----------------------------------------------------------------------

    def onChallenge(self, challenge):

        log.debug('onChallenge -------------------------------------------')

        log.debug("Challenge for method received", authmethod=challenge.method)
        raise Exception("We haven't asked for authentication!")
        log.debug('leaving onChallenge')

        log.debug('onChallenge --------------------------------------------')

    #-----------------------------------------------------------------------

    @defer.inlineCallbacks
    def onJoin(self, details):

        log.debug('onJoin -------------------------------------------------')

        # extra holds arguments for the rpc call
        extra    = self.config.extra
        rpc_url  = next(iter(extra))
        a        = extra[rpc_url] # nav dictionary

        #print('rpc_url: %s', rpc_url, 'a: %s', a)

        try:
            log.debug('entered KikisSession onJoin try block...')
            log.debug('about to block on yield...')

            res = yield self.call(rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], a[6],
                      a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL' )

            #result = threads.blockingCallFromThread(
            #    reactor, getPage, "http://twistedmatrix.com/")

            #res = threads.blockingCallFromThread(
            #         reactor, self.call, rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], a[6],
            #          a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL' )

            log.debug('back from yield...')
            #print(res)

            log.debug('assigning result to self.config.extra')
            self.config.extra[u'result'] = res

            #log.debug('onJoin ----------------------------------------------')
            #reactor.stop()

            log.debug('onJoin ---------------------------------------------')
            #reactor.callFromThread(reactor.stop)
            #self.leave()

        except ApplicationError as e:
            ## ignore errors due to the frontend not yet having
            ## registered the procedure we would like to call
            if e.error != 'wamp.error.no_such_procedure':
                log.debug('onJoin -------------------------------------------')
                self.leave()
                #raise e

        except ReactorNotRestartable as e:
            log.debug( "caught exception %s", e)
            self.leave()
            #raise e

        except Exception as e:
            #raise error.ReactorNotRestartable()
            #except ReactorNotRestartable as e:
            log.debug( "caught exception %s", e)
            log.debug('onJoin ------------------------------------------------')
            self.leave()

        reactor.callFromThread(reactor.stop)

    #-----------------------------------------------------------------------

    def onLeave(self, details):

        log.debug('onLeave ---------------------------------------------------')

        #reactor.callFromThread(reactor.stop)

        self.log.info("local py Router session closed ({details})", details=details)
        log.debug('calling self.disconnect()')

        log.debug('onLeave ---------------------------------------------------')
        self.disconnect()

    #-----------------------------------------------------------------------

    def onDisconnect(self):

        log.debug('onDisconnect ----------------------------------------------')

        try:
            log.debug('called reactor.stop()' )
            reactor.stop()
            log.debug('onDisconnect ------------------------------------------')

        except ReactorNotRunning:
            log.debug('caught ReactorNotRunning, pass ' )
            log.debug('onDisconnect ------------------------------------------')
            pass
            #exit()
