#----------------------------------------------------------------------------------

"""
    getter_setter_11_30.py

    This file holds the get and set (eventually perhaps the pub and sub) routines.

    The supporting code resides here for now; for example the code for creating the
    arguments to the call() component method will be in this file.

"""

#----------------------------------------------------------------------------------

from kikis.kikis_event_03_20 import remote_event

INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

"""
    rpc_arg_prep

        This routine just prepares the data to be passed to the 
        remote proceedcure.

"""

#----------------------------------------------------------------------------------

def rpc_arg_prep (opp, key, value,  path):

    sub = u"rpc_arg_prep"
    print(">>> entered ", sub )

    print("\nopp:       ", opp,   "\n")
    print("key:         ", key,   "\n")
    print("value:       ", value, "\n")
    print("path:        ", path,  "\n")

    #if ( opp ==  u"get" ): 


    a = []
    a.append(u"operation")
    a.append(opp)
    a.append(u"key")
    a.append(key)
    a.append(u"value")
    a.append(value)

    alen = len(a)

    for d in path:
        for key, value in d.items():
            a.append(key)
            a.append(value)

            print('----------------------------')
            print('key: ', key, ' value: ', value)
            print('----------------------------')


    alen = len(a)

    
    print('----------------------------')
    print('length of a:', alen )
    print('----------------------------')
    
    add_nulls = INPUT_ARRAY_SIZE - alen

    for x in range(add_nulls):
        a.append(u'NULL')
        #a.append(None)

    print('----------------------------')
    print ("a: ", a )
    print('----------------------------')

    print (">>> exiting ", sub )
    return a


#----------------------------------------------------------------------------------

"""

    get_elememnt_value:

        This routine sends the remote procedure call to the crossbar server.

"""

#----------------------------------------------------------------------------------

def get_item_value(key, path):

    sub = u"get_item_value"
    print(">>> entered ", sub )

    rpc_url = u"com.kikis.get"  # URI to rpc
    value   = u'NULL'           # value is a NULL string in get opperation

    # prep arguments to the 'get' RPC opperation
    msg = rpc_arg_prep(u"get", key, value,  path)    # formats the msg
    print("msg: ", msg )


    print(">>> ", sub, " calling remote_event()" )
    res = remote_event( rpc_url, msg )

    #print ( ">>> ", sub, "returning the result", res )
    print(">>> exiting ", sub )
    return res


#----------------------------------------------------------------------------------

"""

    set_elememnt_value:

        This routine sends the remote procedure call to the crossbar server.

"""

#----------------------------------------------------------------------------------

def set_element_value(key, path):

    sub = u"set_element_value"
    print(">>> entered ", sub )

    # prep arguments to the 'set' RPC
    rpc_url = u"com.kikis.set"
    a       = rpc_arg_prep(u"set", key, path) 


    print(">>> ", sub, " calling remote_event()" )
    res = remote_event( rpc_url, a )

    #print ( ">>> ", sub, "returning the result", res )
    print(">>> exiting ", sub )
    return res

#----------------------------------------------------------------------------------
