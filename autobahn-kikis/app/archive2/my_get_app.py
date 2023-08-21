
import os
import txaio

#ReactorNotRestartable
from twisted.internet import defer
#from kikis.KikisSessionWrapper import KikisSession
from autobahn.twisted.wamp import ApplicationRunner, ApplicationSession
from twisted.internet.error import ReactorNotRunning
from autobahn.wamp.exception import ApplicationError
from twisted.internet import reactor

# simple logging
import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


#from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory

from kikis.getter_setter import get_element_value, rpc_arg_prep
#from kikis.kikis_thread import  KikisBaseClient

from kikis.KikisSessionWrapper import KikisSession
from autobahn.twisted.wamp import ApplicationRunner, ApplicationSession
from twisted.internet.error import ReactorNotRunning
from twisted.internet import reactor


#----------------------------------------------------------------------------------

"""

    my_get_app.py

        Test application for the 'get' command


"""

#----------------------------------------------------------------------------------

if __name__ == '__main__':

    log.debug('start' )

    # currently CBURL and CBREALM are set probably by docker

    url   = None
    realm = None

    rpc_url       = u"com.kikis.get"
    url         = os.environ.get('CBURL', url )
    realm       = os.environ.get('CBREALM', realm )

    a             = []
    extra_d       = { rpc_url : a }

    #log.debug( "realm:  %s", realm)
    #log.debug( "url:    %s", url )


    # define 'vs_path'. This creates a resuable path to a UI element in the
    # remote Windows host's UI Tree.  Defines a region in the Tree  

    vs_path  = []
    vs_path.append({ u'UIA_NameProperty' : u'Taskbar' })
    vs_path.append({ u'UIA_NameProperty' : u'Running applications' })
    vs_path.append({ u'UIA_NameProperty' : u'Visual Studio 2017 - 1 running window' })

    #log.debug('\nvs_path:', vs_path, '\n')

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

    # call get_element_value() and log the result - twice

    log.debug('>>> calling first time: ')
    res1 = get_element_value( nm );
    log.debug('RESULT 1: %s', res1)

    #----------------------------------------------------------------------------------

    #log.debug('>>> calling sectond time: ')
    #res2 = get_element_value( fo );
    #log.debug('RESULT 2: %s', res2)

    #----------------------------------------------------------------------------------

    # other test data
    #ld.append({ u'get' : u'UIA_NameProperty' })
    #ld.append({ u'get' : u'UIA_TextPatternId' })
    #ld.append({ u'get' : u'UIA_IsEnabledProperty' })
    #ld.append({ u'get' : u'UIA_HasKeyboardFocusProperty'})
    #ld.append({ u'get' : u'UIA_IsKeyboardFocusableProperty' })

#----------------------------------------------------------------------------------
