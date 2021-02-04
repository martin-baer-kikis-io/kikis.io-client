"""
----------------------------------------------------------------------------------

    IUIAutomation.py

        runs the WAMP Client

----------------------------------------------------------------------------------
"""
import os
import sys
import argparse
import six
import txaio
import time

from autobahn.twisted.util import sleep
from autobahn.wamp.types import RegisterOptions
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

#from autobahn.twisted.component import Component
#from twisted.internet import reactor

#from collections import OrderedDict

from kikis.ClientSessionWrapper_5_13 import ClientSession

INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

def process_commandline_arguments ( url, realm ):

    # parse command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument ('-d', '--debug',
                         action='store_true',
                         help='Enable debug output.')

    parser.add_argument ('--url', dest='url',
                         type=six.text_type,
                         default=url,
                         help='The router URL (default: "ws://masterdns.kikis.local:8080/ws").')

    parser.add_argument ('--realm',
                         dest='realm',
                         type=six.text_type,
                         default=realm,
                         help='The realm to join (default: "realm1").')

    return parser.parse_args()

#----------------------------------------------------------------------------------

#def get( args, ld ):
def get( ld ):

    # set default values for commandline arguments
    url   = "ws://masterdns.kikis.local:8080/ws"
    realm = "realm1"
    args = process_commandline_arguments ( url, realm )


    # start logging
    if args.debug:
        txaio.start_logging(level='debug')
    else:
        txaio.start_logging(level='info')

    #
    # Crossbar.io connection configuration
    #

    url   = os.environ.get('CBURL', args.url ) 
    realm = os.environ.get('CBREALM', args.realm )


    #
    # Add the list argument to the extra dictionary
    #

    extra_dict = {u'nav_ld': ld, u'rpc_url': u'com.kikis.get'}

    #
    # now actually run a WAMP client using our session class ClientSession
    #

    #----------
    # new attempt to restart event loop
    #import sys
    #del sys.modules['twisted.internet.reactor']
    #from twisted.internet import reactor
    #from twisted.internet import default
    #default.install()
    #----------

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    runner.run(ClientSession, auto_reconnect=True)
    return runner.extra[u'result']

    #component = Component(transports=url, realm=realm, extra=extra_dict )
    #comp_d = component.start(reactor)
    #transports=u"ws://localhost:8080/ws",
    #realm=u"crossbardemo",
    #)
    #return component.extra[u'result']


#----------------------------------------------------------------------------------

def set( args, nav_list):

    # set default values for commandline arguments
    url   = "ws://masterdns.kikis.local:8080/ws"
    realm = "realm1"
    args = process_commandline_arguments ( url, realm )

    # start logging
    if args.debug:
        txaio.start_logging(level='debug')
    else:
        txaio.start_logging(level='info')


    #
    # Crossbar.io connection configuration
    #

    url   = os.environ.get('CBURL', args.url )
    realm = os.environ.get('CBREALM', args.realm )

    #
    # Add the list argument to the extra dictionary
    #

    extra_dict = {u'navigation_list': nav_list }

    #
    # Run a WAMP client using our session class ClientSession
    #

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict)
    runner.run(ClientSession, auto_reconnect=True)

    return runner.extra[u'result']

#----------------------------------------------------------------------------------
