#----------------------------------------------------------------------------------

"""
    getter_setter_11_30.py

    This file holds the get and set (eventually perhaps the pub and sub) routines.

    The supporting code resides here for now; for example the code for creating the
    arguments to the call() component method will be in this file.

"""

#----------------------------------------------------------------------------------

from kikis.kikis_event_11_30 import remote_event

INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

"""
    rpc_arg_prep

        This routine just prepares the data to be passed to the 
        remote proceedcure.

"""

#----------------------------------------------------------------------------------

def rpc_arg_prep (ld):

    sub = u"rpc_arg_prep"
    print(">>> entered ", sub )
    #print("\nld:        ", ld, "\n")

    a = []
    for d in ld:
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

    #print('----------------------------')
    #print ("a: ", a )
    #print('----------------------------')

    print (">>> exiting ", sub )
    return a


#----------------------------------------------------------------------------------

"""

    get_elememnt_value:

        This routine sends the remote procedure call to the crossbar server.

"""

#----------------------------------------------------------------------------------

def get_element_value(ld):

    sub = u"get_element_value"
    print(">>> entered ", sub )

    # prep arguments to the 'get' RPC
    rpc_url = u"com.kikis.get"
    a       = rpc_arg_prep(ld) 

    print(">>> ", sub, " calling remote_event()" )
    res = remote_event( rpc_url, a )

    #print ( ">>> ", sub, "returning the result", res )
    print(">>> exiting ", sub )
    return res


#----------------------------------------------------------------------------------

def set_element_value(ld):

    sub = u"set_element_value"
    print("entered ", sub )

    # prep arguments to the 'set' RPC
    rpc_url = u"com.kikis.set"
    a       = rpc_arg_prep(ld) 

    #print("calling event()" )
    #event( rpc_url, a )

    #print("calling remote_event()" )
    print("leaving ", sub )
    #remote_event( rpc_url, a )


#----------------------------------------------------------------------------------
