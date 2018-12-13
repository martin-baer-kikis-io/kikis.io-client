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

from autobahn.twisted.util import sleep
from autobahn.wamp.types import RegisterOptions
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

from kikis.ClientSessionWrapper import ClientSession

INPUT_ARRAY_SIZE = 16


#----------------------------------------------------------------------------------
def get( args, nav_list):

    #
    # Crossbar.io connection configuration
    #

    url   = os.environ.get('CBURL', args.url ) 
    realm = os.environ.get('CBREALM', args.realm )


    # add the list argument to the extra dictionary

    extra_dict = {u'navigation_list': nav_list }

    #
    # now actually run a WAMP client using our session class ClientSession
    #

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    runner.run(ClientSession, auto_reconnect=True)

    res = runner.extra[u'result']

    print('-------------------------------------------------------------------------------------')
    print('get result:  ', res )
    print('-------------------------------------------------------------------------------------')

    return res
    



#----------------------------------------------------------------------------------
def set( args, nav_list):

    #
    # Crossbar.io connection configuration
    #

    url   = os.environ.get('CBURL', args.url )
    realm = os.environ.get('CBREALM', args.realm )

    # add the list argument to the extra dictionary
    extra_dict = {u'navigation_list': nav_list }

    #
    # now actually run a WAMP client using our session class ClientSession
    #

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict)
    runner.run(ClientSession, auto_reconnect=True)

    res = runner.extra[u'result']

    print('-------------------------------------------------------------------------------------')
    print('set result:  ', res )
    print('-------------------------------------------------------------------------------------')

    return res
    

