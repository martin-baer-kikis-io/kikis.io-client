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

# simple debug logging
import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

from twisted.web.client import getPage
from twisted.web.error import Error

from twisted.internet import threads, reactor, defer
from autobahn.twisted.wamp import ApplicationRunner
from kikis.KikisThreadedSessionWrapper import KikisThreadedSession

#----------------------------------------------------------------------------------

def thread_stuff(session):

    sub = "thread_stuff"
    log.debug('enter %s', sub )

    # session.config: ComponentConfig(realm=<default>, extra=None, keyring=None,
    # controller=None, shared=None)

    #log.debug('session.config: %s', session.config  )
    #exit()

    #orig = FUNC_ARGS['resultTopic']
    #session.config.extra['joined'].wait()

    log.debug('calling do_work using callFromThread' )
    #res = reactor.callFromThread(session.do_work,args )
    #res = reactor.callFromThread(session.do_work)
    log.debug('back from call to do_work using callFromThread' )

    #log.debug('calling do_work using callInThread' )
    #res = reactor.callInThread(session.do_work, args)
    #log.debug('back from calling do_work using callInThread' )

    #result = session.config.extra['result_queue'].get()
    #reactor.callFromThread(reactor.stop())

    #log.debug('returning res:  %s', res)
    log.debug('leave %s', sub )
    #return res
    return

#----------------------------------------------------------------------------------
def inThread():

    sub = "inThread"
    log.debug('enter %s', sub )

    from twisted.internet import threads, reactor, defer

    try:
        result = threads.blockingCallFromThread(
            reactor, getPage, b"http://www.kikis.tv/")
    except Error as exc:
        log.debug( "exec :", exc )
    else:
        log.debug( "exec :", result)

    reactor.callFromThread(reactor.stop)
    log.debug('leave %s', sub )

#----------------------------------------------------------------------------------


def remote_threaded_event(rpc_url, a):

    sub = "remote_threaded_event"
    log.debug('enter %s', sub )

    # currently CBURL and CBREALM are set probably by docker

    url   = None
    realm = None

    url        = os.environ.get('CBURL', url )
    realm      = os.environ.get('CBREALM', realm )
    extra_d = { rpc_url : a }
    log.debug ( 'extra_d:    %s', extra_d)

    log.debug ( 'realm:      %s', realm )
    log.debug ( 'url:        %s', url )
    log.debug ( 'rpc_url:    %s', rpc_url )

#----------------------------------------------------------------------------------

    from twisted.internet import threads, reactor, defer

    log.debug("creating runner")
    runner = ApplicationRunner(url=url, realm=realm, extra=extra_d )

    log.debug("creating threaded session object")
    session = KikisThreadedSession()

    log.debug("initializing threaded session data")
    session.config.realm = realm 
    session.config.extra = extra_d
    #log.debug('session.config: %s', session.config  )
    #exit()

    log.debug("creating thread t with target=thread_stuff")
    t = threading.Thread(target=thread_stuff, args=(session,))

    log.debug("starting thread t")
    t.start()

    log.debug("runner.run")
    runner.run(session)

    exit();

    log.debug("reactor.callFromThread()")
    reactor.callFromThread(inThread)

    log.debug("reactor.run()")
    reactor.run()

    log.debug("reactor.stop()")
    reactor.stop()

    res = runner.extra[u'result']
    log.debug("res: %s", res)

    log.debug("calling t.join()")
    t.join()

    log.debug('leave %s', sub )
    return res

