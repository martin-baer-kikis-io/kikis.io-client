import os 
import argparse
import six
import txaio

from twisted.internet import reactor
from twisted.internet.error import ReactorNotRunning
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.wamp.types import RegisterOptions
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

from dev import ClientSession

# was main of oiginal ClientSession call....


# Crossbar.io connection configuration
# url = os.environ.get('CBURL', u'ws://localhost:8080/ws')
url = os.environ.get('CBURL', u'ws://masterdns.kikis.local:8080/ws')
realm = os.environ.get('CBREALM', u'realm1')

"""
# parse command line parameters
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output.')

parser.add_argument('--url', dest='url', type=six.text_type, default=url, help='The router URL (default: "ws://masterdns.kikis.local:8080/ws").')

parser.add_argument('--realm', dest='realm', type=six.text_type, default=realm, help='The realm to join (default: "realm1").')

args = parser.parse_args()

# start logging
if args.debug:
txaio.start_logging(level='debug')
else:
txaio.start_logging(level='info')

# any extra info we want to forward to our ClientSession (in self.config.extra)
extra = {
u'method': u'AddAutomationEventHandler',
u'message': u'message'
}
"""


# now actually run a WAMP client using our session class ClientSession
runner = ApplicationRunner(url=args.url, realm=args.realm, extra=extra)
runner.run(ClientSession, auto_reconnect=True)
