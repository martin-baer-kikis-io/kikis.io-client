#----------------------------------------------------------------------------------
"""
    kikis_event_11_30.py

    This file holds the code for remote_event(). 

    The component will need to be updated to use the factory style.

"""

#----------------------------------------------------------------------------------

import os
import txaio
from autobahn.twisted.wamp import ApplicationRunner
from kikis.KikisSessionWrapper import KikisSession

#----------------------------------------------------------------------------------

"""

    remote_event()

        This routine sends an rpc request with the autobahn call() proceedure.
"""

#----------------------------------------------------------------------------------


def remote_event(rpc_url, a):

    sub = u"remote_event"
    print(">>> entered ", sub )

    # currently CBURL and CBREALM are set probably by docker

    url   = None
    realm = None

    url        = os.environ.get('CBURL', url )
    realm      = os.environ.get('CBREALM', realm )
    extra_dict = { rpc_url : a }

    """
    print( ">>> realm:  ", realm)
    print( ">>> url:    ", url )
    """

    # working - but old style

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    runner.run(KikisSession, auto_reconnect=True)
    res = runner.extra[u'result']

    print(">>> leaving", sub )
    return res

