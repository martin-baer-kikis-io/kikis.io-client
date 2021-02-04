#----------------------------------------------------------------------------------
"""
    kikis_event_11_30.py

    This file holds the code for remote_event(). 

    The component will need to be updated to use the factory style.

"""

#----------------------------------------------------------------------------------

import os
import txaio
import threading

from twisted.web.client import getPage
from twisted.web.error import Error

#from twisted.internet import threads, reactor, defer
from autobahn.twisted.wamp import ApplicationRunner
from kikis.KikisThreadedSessionWrapper import KikisThreadedSession

#----------------------------------------------------------------------------------

def threadstuff(session):

    pass

    #orig = FUNC_ARGS['resultTopic']
    session.config.extra['joined'].wait()
    reactor.callFromThread(session.do_work, FUNC_ARGS)
    result = session.config.extra['result_queue'].get()
    reactor.callFromThread(reactor.stop())
    #reactor.stop()
    #for i in xrange(100):
    #    #FUNC_ARGS['resultTopic'] = orig + ('.%d' % i)
    #   #start = time.time()
    #   #reactor.callFromThread(session.do_work, FUNC_ARGS)
    #   #esult = session.config.extra['result_queue'].get()
    #   #end = time.time()
    #   #print time.sleep(1)  # minisleep for tcpdump logging delay
    #   #print 'Result: %s (%.2fs)' % (result, end - start)
    #   #print '\nSleeping\n'
    #   #time.sleep(6)
    #   #print '\nDone Sleeping\n'


#----------------------------------------------------------------------------------
def inThread():

    from twisted.internet import threads, reactor, defer

    try:
        result = threads.blockingCallFromThread(
            reactor, getPage, b"http://www.kikis.tv/")
    except Error as exc:
        print ( "exec :", exc )
    else:
        print ( "exec :", result)

    reactor.callFromThread(reactor.stop)

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

    #print( ">>> realm:  ", realm)
    #print( ">>> url:    ", url )

#----------------------------------------------------------------------------------
    # working - but old style

    #runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    #runner.run(KikisSession, auto_reconnect=True)

#----------------------------------------------------------------------------------
# reference to changes
# https://stackoverflow.com/questions/28414302/how-create-a-python-application-with-two-thread-each-which-has-a-autobahn-applic
#def __init__(self):
#    self.runner = ApplicationRunner(url=wampAddress, realm=wampRealm)
#
#def start(self):
#    # Pass start_reactor=False to all runner.run() calls
#    self.runner.run(AutobahnMRS, start_reactor=False)

#----------------------------------------------------------------------------------

    from twisted.internet import threads, reactor, defer

    reactor.callFromThread(inThread)
    reactor.run()
    reactor.stop()

    #reactor.callFromThread(inThread)
    #reactor.run()
    #reactor.stop()
    #exit()

    runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    #runner.run(AutobahnMRS, start_reactor=False)
    #t = threading.Thread(target=threadstuff, args=(KikisThreadedSession,auto_reconnect=False,start_reactor=False,))
    #t = threading.Thread(target=threadstuff, args=(KikisThreadedSession,))
    t = threading.Thread(target=inThread,)
    t.start()

    #runner.run(session)
    #runner.run(KikisThreadedSession, start_reactor=False, auto_reconnect=False)
    runner.run(KikisTheadedSession)

    # Pass start_reactor=False to all runner.run() calls
    #runner.run(KikisThreadedSession, start_reactor=False, auto_reconnect=False)

    # here or somewhere else?
    from twisted.internet import reactor
    #reactor.run()
    #reactor.callFromThread(reactor.stop())

#----------------------------------------------------------------------------------

    #runner = ApplicationRunner(url=url, realm=realm, extra=extra_dict )
    #runner.run(KikisThreadedSession, auto_reconnect=True)

#----------------------------------------------------------------------------------

    res = runner.extra[u'result']

    t.join()

    print(">>> leaving", sub )
    return res

