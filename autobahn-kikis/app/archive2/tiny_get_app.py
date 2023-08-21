
from autobahn.twisted.component import Component, run
from autobahn.twisted.util import sleep
from twisted.internet.defer import inlineCallbacks
from autobahn.wamp.exception import ApplicationError
import os
import argparse
import six

url = os.environ.get('CBURL', u'ws://localhost:8080/ws')
realmv = os.environ.get('CBREALM', u'realm1')
print(url, realmv)
component = Component(transports=url, realm=realmv)

#----------------------------------------------------------------------------------

INPUT_ARRAY_SIZE = 16

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

def get_test_data ():

    # define 'vs_path'. This creates a resuable path to a UI element in the
    # remote Windows host's UI Tree.  

    vs_path  = []
    vs_path.append({ u'UIA_NameProperty' : u'Taskbar' })
    vs_path.append({ u'UIA_NameProperty' : u'Running applications' })
    vs_path.append({ u'UIA_NameProperty' : u'Visual Studio 2017 - 1 running window' })

    #print ('\nvs_path:', vs_path, '\n')

#----------------------------------------------------------------------------------

    # make a list to u'get' the 'UIA_NameProperty' at the 'vs_path' location in
    # the remote Windows UI Tree. 
    #
    # format:
    #
    #   [u'get' | u'set'], [remote property or value name string ], [path to element] 
    #

    nm = []
    nm.append({ u'get' : u'UIA_NameProperty' })
    #nm.append({ u'bet' : u'UIA_NameProperty' })
    nm.extend( vs_path )

#----------------------------------------------------------------------------------

    # create a second new list with 'get' as first element and append vs_path
    # to test the generator

    fo = []
    fo.append({ u'get' : u'UIA_HasKeyboardFocusProperty'})
    fo.extend( vs_path )

#----------------------------------------------------------------------------------

@component.on_join
@inlineCallbacks
def joined(session, details):
    print("session ready")

    # prep arguments to the 'get' RPC
    rpc_url = u"com.kikis.get"
    a       = rpc_arg_prep(ld)

    try:

        res = yield self.call(rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL' )

        print ("res: ", res );

    except ApplicationError as e:
        ## ignore errors due to the frontend not yet having
        ## registered the procedure we would like to call
        if e.error != 'wamp.error.no_such_procedure':
            session.disconnect()
            raise e

#----------------------------------------------------------------------------------

if __name__ == "__main__":

    sub = "__main__"
    print ('\n\n\n>>> entering ', sub )

    run([component])
