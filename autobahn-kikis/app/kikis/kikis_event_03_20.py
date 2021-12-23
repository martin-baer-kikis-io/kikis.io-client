#----------------------------------------------------------------------------------
"""
    kikis_event_11_30.py

    This file holds the code for remote_event(). 

    The component will need to be updated to use the factory style.

"""

#----------------------------------------------------------------------------------

import os
import txaio
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from autobahn.twisted.wamp import ApplicationRunner
from kikis.KikisSessionWrapper_03_20 import KikisSession

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
    extra      = { rpc_url : a}

    #"""
    print( ">>> realm:  ", realm)
    print( ">>> url:    ", url )
    print( ">>> extra:    ", extra)
    #"""


    t_arg_d  =  { u'url' : url, u'realm' : realm, u'extra' : extra }

    # create and exectute a thread
    #
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    future = executor.submit(event_thread, t_arg_d)
    #    res = future.result()
    #    #print(res)
    #    return res


    # process version

    with ProcessPoolExecutor(max_workers=3) as executor:
        future = executor.submit(event_thread, t_arg_d)
        res = future.result()
        #print(res)
        return res

def event_thread (t_arg_d):

    sub = u"event_thread"

    # execute the thread

    url      = t_arg_d[u'url']
    realm    = t_arg_d[u'realm']
    extra    = t_arg_d[u'extra']

    runner = ApplicationRunner(url=url, realm=realm, extra=extra )
    #runner.run(KikisSession, auto_reconnect=True)
    runner.run(KikisSession, auto_reconnect=False)
    res = runner.extra[u'result']

    print(">>> leaving", sub )
    return res


