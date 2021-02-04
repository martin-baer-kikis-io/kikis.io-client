
from os import environ
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

#import time
import twisted.internet
 
from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver
 

class Component(ApplicationSession):
    """
    An application component using the time service.
    """

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        try:
            #yield self.call(u'com.timeservice.now')
            #res = yield self.call(u'com.kikis.get', u'NULL' )
            yield self.call(u'com.kikis.get', u'NULL' )
            #, u'NULL', u'NULL', u'NULL', u'NULL', u'NULL', u'NULL', u'NULL', u'NULL', u'NULL')
        #print("res: ", res )

        except Exception as e:
            print("Error: {}".format(e))
        else:
            print("Current time from time service: {}".format(now))

        self.leave()

    def onDisconnect(self):
        print("disconnected")
        reactor.stop()


#if __name__ == '__main__':

def test():
    
    #import six
    url   = None
    realm = None
    url        = environ.get('CBURL', url )
    realm      = environ.get('CBREALM', realm )
   
    #url = environ.get("CBURL", u"ws://127.0.0.1:8080/ws")
    #if six.PY2 and type(url) == six.binary_type:
    #    url = url.decode('utf8')
    #realm = u"crossbardemo"
    

    try:
        reactor.run()
       
    except Exception as e:
        print("call error: {0}".format(e))
        print("calling leave in exception block")
        #print e
        import sys
        del sys.modules['twisted.internet.reactor']
        from twisted.internet import reactor
        from twisted.internet import default
        default.install()

    runner = ApplicationRunner(url, realm)
    runner.run(Component)

