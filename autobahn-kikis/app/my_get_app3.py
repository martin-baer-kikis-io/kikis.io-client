from os import environ
from autobahn.twisted.component import Component
from twisted.internet.defer import inlineCallbacks, Deferred
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.web.server import Site
from twisted.internet.task import react

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from kikis.KikisSessionWrapper import KikisSession



"""

# pip install klein
#from klein import Klein


class WebApplication(object):
    
    #A simple Web application that publishes an event every time the
    url "/" is visited.
   
    def __init__(self, app, wamp_comp):
        self._app = app
        self._wamp = wamp_comp
        self._session = None  # "None" while we're disconnected from WAMP router

        # associate ourselves with WAMP session lifecycle
        self._wamp.on('join', self._initialize)
        self._wamp.on('leave', self._uninitialize)
        # hook up Klein routes
        self._app.route(u"/", branch=True)(self._render_slash)

    def _initialize(self, session, details):
        print("Connected to WAMP router")
        self._session = session

    def _uninitialize(self, session, reason):
        print(session, reason)
        print("Lost WAMP connection")
        self._session = None

    def _render_slash(self, request):
        if self._session is None:
            request.setResponseCode(500)
            return b"No WAMP session\n"
        self._session.publish(u"com.myapp.request_served")
        return b"Published to 'com.myapp.request_served'\n"

"""


@inlineCallbacks
def main(reactor):

# -----------------------------------------------------
    print( "entering main object")

    rpc_url = u"com.kikis.get"

    # currently CBURL and CBREALM are set probably by docker
    server_url   = None
    #server_url   = os.environ.get('CBURL', url )
    server_url   = environ.get('CBURL', server_url )

    realm = None
    #realm = os.environ.get('CBREALM', realm )
    realm = environ.get('CBREALM', realm )

    print( "realm:  ", realm)
    print( "server_url:    ", server_url )

    #extra_dict = { rpc_url : a }
    extra_dict = { rpc_url : u"a" }
    print ( "extra_dict type: ", type(extra_dict) )

    #comp = Component(
    #        transports=server_url,
    #        realm=realm,
    #        extra=extra_dict
    #)

    #url = environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8080/ws")
    #if six.PY2 and type(url) == six.binary_type:
    #    url = url.decode('utf8')
    #realm = u"crossbardemo"

    #runner = ApplicationRunner(server_url, realm, extra_dict)

    #component = Component( session_factory=ApplicationRunner(url=server_url, realm=realm, extra=extra_dict ))

    #runner.run(Component)

    #runner = ApplicationRunner(server_url, realm, extra_dict)
    #runner.run(Component)

# -----------------------------------------------------

    print ( "constructing the component" )
    component = Component(
        transports=server_url,
        realm=realm,
        extra=extra_dict
    )
    #app = Klein()
    #webapp = WebApplication(app, component)

    # have our Web site listen on 8090
    #site = Site(app.resource())
    #server_ep = TCP4ServerEndpoint(reactor, 8090)
    #port = yield server_ep.listen(site)
    #print("Web application on {}".format(port))

    # we don't *have* to hand over control of the reactor to
    # component.run -- if we don't want to, we call .start()
    # The Deferred it returns fires when the component is "completed"
    # (or errbacks on any problems).

    print ( "calling component.start.reactor" )
    comp_d = component.start(reactor)
    print ( "back from component.start.reactor" )

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
    print ( "calling Deferred()" )
    done = Deferred()
    print ( "waiting on Deferred()" )
    yield done
    print ( "done waiting on Deferred()" )


if __name__ == '__main__':
    print ( "entering __main__" )
    print ( "calling react.main" )
    react(main)
    print ( "back from react.main" )

