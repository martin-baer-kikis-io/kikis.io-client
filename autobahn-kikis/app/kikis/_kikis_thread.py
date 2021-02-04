from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
import threading
import logging
log = logging.getLogger(__name__)

# ----- twisted ----------
class _WebSocketClientProtocol(WebSocketClientProtocol):
    def __init__(self, factory):
        self.factory = factory

    def onOpen(self):
        log.debug("Client connected")
        self.factory.protocol_instance = self
        self.factory.base_client._connected_event.set()

class _WebSocketClientFactory(WebSocketClientFactory):
    def __init__(self, *args, **kwargs):
        WebSocketClientFactory.__init__(self, *args, **kwargs)
        self.protocol_instance = None
        self.base_client = None

    def buildProtocol(self, addr):
        return _WebSocketClientProtocol(self)
# ------ end twisted -------

class KikisBaseClient(object):

    def __init__(self, **websocket_settings):
    #def __init__(self, url, realm):
        self.settings = websocket_settings
        #self.settings       = []
        #self.settings.append({ u'url' : url })
        #self.settings.append({ u'realm' : realm})

        # instance to be set by the own factory
        self.factory = None
        # this event will be triggered on onOpen()
        self._connected_event = threading.Event()
        # queue to hold not yet dispatched messages
        #self._send_queue = Queue.Queue()
        self._reactor_thread = None

    def connect(self):
        log.debug("Connecting to %(url)s:%(realm)s" % self.settings)
        #log.debug("Connecting to url: ", self.settings )
        #log.debug("Connecting to realm: ", self.settings )
        #self.factory = _WebSocketClientFactory(&  "ws://%(host)s:%(port)dr % self.settings, debug=True)
        #self.factory = _WebSocketClientFactory( "url: %(url) realm: %(realm)" % self.url % self.realm, debug=True)
#        self.factory = _WebSocketClientFactory(
#                                 "url: %(url)s realm: %(realm)s" % self.settings,
#                                 debug=True)
        self.factory = _WebSocketClientFactory(
                                "ws://%(url)s:%(realm)s" % self.settings)
#                                debug=True)

        self.factory.base_client = self
        c = connectWS(self.factory)
        self._reactor_thread = threading.Thread(target=reactor.run,
                                               args=(False,))
        self._reactor_thread.daemon = True
        self._reactor_thread.start()

    def send_message(self, body):
        if not self._check_connection():
            return
        log.debug("Queing send")
        self._send_queue.put(body)
        reactor.callFromThread(self._dispatch)

    def _check_connection(self):
        if not self._connected_event.wait(timeout=10):
            log.error("Unable to connect to server")
            self.close()
            return False
        return True

    def _dispatch(self):
        log.debug("Dispatching")
        #while True:
        #    try:
        #        body = self._send_queue.get(block=False)
        #    except Queue.Empty:
        #        break
        #    self.factory.protocol_instance.sendMessage(body)

    def close(self):
        reactor.callFromThread(reactor.stop)
