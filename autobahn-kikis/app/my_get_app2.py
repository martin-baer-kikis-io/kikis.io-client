
from os import environ
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
	

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
	

	

class Component(ApplicationSession):
    """
    An application component using the time service.
    """
	
    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        try:
            #res = yield self.call(u'com.timeservice.now')
            res = yield self.call(details.extra.rpc_url)
        except Exception as e:
            print("Error: {}".format(e))
        else:
            print("Current time from time service: {}".format(res))
	

        self.leave()
	

    def onDisconnect(self):
        print("disconnected")
        reactor.stop()
	

	

if __name__ == '__main__':
    import six
    rpc_url = u"com.kikis.get"

    # currently CBURL and CBREALM are set probably by docker
    url   = None
    #url   = os.environ.get('CBURL', url )
    url   = environ.get('CBURL', url )

    realm = None
    #realm = os.environ.get('CBREALM', realm )
    realm = environ.get('CBREALM', realm )

    print( "realm:  ", realm)
    print( "\nurl:    ", url )

    #extra_dict = { rpc_url : a }
    extra_dict = { rpc_url : u"a" }
    #print ( "type: ", type(extra_dict) )

    #comp = Component(
    #        transports=url,
    #        realm=realm,
    #        extra=extra_dict
    #)

    #url = environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8080/ws")
    #if six.PY2 and type(url) == six.binary_type:
    #    url = url.decode('utf8')
    #realm = u"crossbardemo"

    #runner = ApplicationRunner(url, realm, extra_dict)
    component = Component( session_factory=ApplicationRunner(url=url, realm=realm, extra=extra_dict ))
    runner.run(Component)

    #runner = ApplicationRunner(url, realm, extra_dict)
    runner.run(Component)


