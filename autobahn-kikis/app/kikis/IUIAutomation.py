"""
----------------------------------------------------------------------------------

    IUIAutomation.py

        runs the WAMP Client

----------------------------------------------------------------------------------
"""
import os
import argparse
import six
import txaio

from autobahn.twisted.util import sleep
from autobahn.wamp.types import RegisterOptions
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

from kikis.ClientSessionWrapper import ClientSession

#----------------------------------------------------------------------------------
def get( args, navigation_dict):

    #
    # Crossbar.io connection configuration
    #

    url   = os.environ.get('CBURL', args.url ) 
    realm = os.environ.get('CBREALM', args.realm )

    #
    # now actually run a WAMP client using our session class ClientSession
    #

    runner = ApplicationRunner(url=url, realm=realm, extra=navigation_dict )
    runner.run(ClientSession, auto_reconnect=True)

    res = runner.extra[u'result']

    print('-------------------------------------------------------------------------------------')
    print('get result:  ', res )
    print('-------------------------------------------------------------------------------------')

    return res
    



#----------------------------------------------------------------------------------
def set( args, navigation_dict):

    #
    # Crossbar.io connection configuration
    #

    url   = os.environ.get('CBURL', args.url )
    realm = os.environ.get('CBREALM', args.realm )

    #
    # now actually run a WAMP client using our session class ClientSession
    #

    runner = ApplicationRunner(url=url, realm=realm, extra=navigation_dict )
    runner.run(ClientSession, auto_reconnect=True)

    res = runner.extra[u'result']

    print('-------------------------------------------------------------------------------------')
    print('set result:  ', res )
    print('-------------------------------------------------------------------------------------')

    return res
    

