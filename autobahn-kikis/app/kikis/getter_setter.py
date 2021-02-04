#----------------------------------------------------------------------------------

"""
    getter_setter.py

    This file holds the get and set (eventually perhaps the pub and sub) routines.
    The supporting code resides here for now; for example the code for creating the
    arguments to the call() component method will be in this file.

"""

#----------------------------------------------------------------------------------

# simple debug logging
import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


#from kikis.kikis_event import remote_event
from kikis.kikis_threaded_event import remote_threaded_event

INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

def rpc_arg_prep (ld):

    sub = "rpc_arg_prep"
    log.debug('start %s', sub)
    #log.debug("ld:        %s", ld)

    a = []
    for d in ld:
        for key, value in d.items():
            #print('key: ', key, ' value: ', value)
            a.append(key)
            a.append(value)

    alen = len(a)
    #rint('length of a: %d', alen )

    add_nulls = INPUT_ARRAY_SIZE - alen

    for x in range(add_nulls):
        a.append(u'NULL')
        
    #rint("a: %s", a )

    log.debug('end %s', sub)
    return a

#----------------------------------------------------------------------------------

def get_element_value(ld):

    sub = 'get_element_value'
    log.debug('start %s', sub)

    # prep arguments to the 'get' RPC
    rpc_url = u"com.kikis.get"
    a       = rpc_arg_prep(ld) 

    #res = remote_event( rpc_url, a )
    res = remote_threaded_event( rpc_url, a )

    #print ( sub, " result: ", res )
    log.debug('end %s', sub )
    return res


#----------------------------------------------------------------------------------

def set_element_value(ld):

    sub = "set_element_value"
    log.debug('start %s', sub)

    # prep arguments to the 'set' RPC
    rpc_url = u"com.kikis.set"
    a       = rpc_arg_prep(ld) 

    #log.debug("calling event()" )
    #event( rpc_url, a )

    #log.debug("calling remote_event()" )
    #remote_event( rpc_url, a )

    log.debug('end %s', sub )


#----------------------------------------------------------------------------------
