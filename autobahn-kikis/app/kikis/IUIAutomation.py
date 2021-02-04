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

from twisted.internet.defer import inlineCallbacks, Deferred
from autobahn.twisted.util import sleep
from autobahn.wamp.types import RegisterOptions
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError
from autobahn.twisted.wamp import ApplicationSession


from autobahn.twisted.component import Component
from autobahn.twisted.component import run


INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

#comp = Component(
#     transports=u"ws://crossbario:8080/ws",
#     realm=u"realm1",
# )
#
#@comp.on_join
#def joined(session, details):
#     print("session ready")
#
#if __name__ == "__main__":
#    run([comp])
#
#system.exit()

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

def get( ld ):

    extra=self.config.extra

    nav_ld = extra[u'nav_ld'] # navigation hops dictionary
    rpc_url  = extra[u'rpc_url']  # 'get' or 'set' instruction

    a = []
    for d in nav_ld:
        for key, value in d.items():
            a.append(key)
            a.append(value)
            #print('----------------------------')
            #print('key: ', key, ' value: ', value)
            #print('----------------------------')

    alen = len(a)
    #print('----------------------------')
    #print('length of a:', alen )
    #print('----------------------------')

    add_nulls = INPUT_ARRAY_SIZE - alen

    for x in range(add_nulls):
        a.append(u'NULL')
        #a.append(None)
        
    rpc_url    = u"com.kikis.get"
    server_url = u"ws://crossbar:8080/ws"
    realm      = u"realm1"

    extra_dict = {u'nav_ld': ld, u'rpc_url': u'com.kikis.get'}

    comp = Component(
        transports= server_url,
        realm=realm,
        extra=extra_dict,
     )

    print ( "here" )

    #@comp.on_connect
    #def connected():
    #    print ( "connected to rpc_url" ) 

    @comp.on_join
    def joined(session, details):
        print("session ready")

    comp_d    = comp.start()

    #print("breezed past joined")
    #$if __name__ == "__main__":
    #    run([comp])
    run([comp])

    #done = Deferred()
    #yield done

    print("breezed past run")

    print("exiting")
    exit()
    print("maybe didn't exit")




    # default values 
    url   = "ws://masterdns.kikis.local:8080/ws"
    realm = "realm1"
    print ("hard coded url: ", url )
    print ("hard coded realm: ", realm)

    # commandline arguments
    args = process_commandline_arguments ( url, realm )
    print ("args coded url: ", args.url )
    print ("args coded realm: ", args.realm)

    # start logging
    if args.debug:
        txaio.start_logging(level='debug')
    else:
        txaio.start_logging(level='info')

    # set by Crossbar.io connection configuration
    url   = os.environ.get('CBURL', args.url ) 
    realm = os.environ.get('CBREALM', args.realm )
    print ("CB env url: ", url)
    print ("CB env realm: ", realm)


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

    #url   = "ws://masterdns.kikis.local:8080/ws"
    print ("using url: ", url," and realm: ",  realm)


    #runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    #runner.run(ClientSession, auto_reconnect=True)
    #return runner.extra[u'result']



    #component = Component( session_factory=ApplicatioinRunner(url=url, realm=realm, extra=extra_dict )) 
    #comp_d    = component.start(reactor)
    #print ("comp_d: ", comp_d )

    #comp_d    = component.start(reactor)
    #component = Component( transports=url, realm=realm ) 
    #component.session_factory=ClientSession(auto_reconnect=True)

    #component.session_factory=ClientSession(runner)
    #component.session_factory=ClientSession
    #comp_d = component.start(reactor)
    #return component.extra[u'result']

    #component = Component(transports=url, realm=realm, extra=extra_dict )
    #comp_d = component.start(reactor)

    #done = Deferred()
    #yield done

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
