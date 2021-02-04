#----------------------------------------------------------------------------------
"""
    getter_setter.py

    This file holds the code for remote_event(). The component will need to
    be updated to use the factory style.

"""

#----------------------------------------------------------------------------------


import os
import txaio


from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from kikis.my_comp import Component

from autobahn.twisted.component import Component
from twisted.internet.defer import inlineCallbacks, Deferred
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.web.server import Site
from twisted.internet.task import react

#----------------------------------------------------------------------------------


def remote_event(rpc_url, a):

    sub = u"remote_event"
    print("entered ", sub )

    # currently CBURL and CBREALM are set probably by docker
    url   = None
    url   = os.environ.get('CBURL', url )

    realm = None
    realm = os.environ.get('CBREALM', realm )

    print( "realm:  ", realm)
    print( "\nurl:    ", url )

    extra_dict = { rpc_url : a }
    print ( "type: ", type(extra_dict) )

    #comp = Component(
    #        transports=url,
    #        realm=realm,
    #        extra=extra_dict
    #)

#----------------------------------------------------------------------------------
    # working

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    runner.run(comp)
    #return runner.extra[u'result']
#----------------------------------------------------------------------------------
    #component = Component( session_factory=ApplicationRunner(url=url, realm=realm, extra=extra_dict ))




#----------------------------------------------------------------------------------

"""

@inlineCallbacks
def main(reactor):

    sub = u"remote_event"
    print("entered ", sub )

    # currently CBURL and CBREALM are set probably by docker
    url   = None
    url   = os.environ.get('CBURL', url )

    realm = None
    realm = os.environ.get('CBREALM', realm )

    rpc_url = u"com.kikis.get"
    
    print( "realm:  ", realm)
    print( "\nurl:    ", url )
    print( "\nrpc_url:    ", rpc_url )
    
    #extra_dict = { rpc_url : a }
    extra_dict = { rpc_url : u"a" }
    print ( "type: ", type(extra_dict) )

    component = Component(
            transports=url,
            realm=realm,
            extra=extra_dict
    )

    # we don't *have* to hand over control of the reactor to
    # component.run -- if we don't want to, we call .start()
    # The Deferred it returns fires when the component is "completed"
    # (or errbacks on any problems).
    comp_d = component.start(reactor)
    
    # When not using run() we also must start logging ourselves.
    import txaio
    txaio.start_logging(level='info')
    
    # If the Component raises an exception we want to exit. Note that
    # things like failing to connect will be swallowed by the
    # re-connection mechanisms already so won't reach here.
    
    def _failed(f):
        print("Component failed: {}".format(f))
        done.errback(f)
    comp_d.addErrback(_failed)
    
    # wait forever (unless the Component raises an error)
    done = Deferred()
    yield done
    
#if __name__ == '__main__':
    react(main)

"""





#----------------------------------------------------------------------------------
"""













def _remote_event(rpc_url, a):

    sub = u"remote_event"
    print("entered ", sub )

    # currently CBURL and CBREALM are set probably by docker
    url   = None
    url   = os.environ.get('CBURL', url )

    realm = None
    realm = os.environ.get('CBREALM', realm )

    print( "\nrealm:  ", realm)
    print( "url:    ", url )


    print( "creating component" )
    comp = Component() 

    #print( "calling component.start()" )
    #comp.start()
    #run([comp])
    #print("leaving ", sub )

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")

#    @comp.on_join

    @inlineCallbacks
    def joined(session, details):
        print("session ready")
        #session.leave()
        session.start()

        try:
            #res = yield session.call(u'com.myapp.add2', 2, 3)
            #res = yield session.call(
            res = yield session.call(
                  rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7],
                  a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL'
                  )

        except Exception as e:
            print("call error: {0}".format(e))
            print("calling leave in exception block")
            session.leave()
            #stop()


            #print("calling leave in joined block")
            #session.leave()
            #stop()
            #print("call result: {}".format(res))
            print("returning result: {}".format(res))


            self.leave()

            return res

#        except Exception as e:
#            print("call error: {0}".format(e))
#            print("calling leave in exception block")
#            session.leave()
#            #stop()


    def onDisconnect(self):
        print("disconnected")
        reactor.stop()


    # connect to the server and join the realm
    #run([comp])
    #comp.start()
    #session.start()
    #print("calling leave right after run")
    #session.leave()

"""
