
import os
import argparse
import six
import txaio

#from kikis.Constants import *
from kikis.IUIAutomation import get

#----------------------------------------------------------------------------------

"""

    my_app.py

        Test application for the get() command


"""

#----------------------------------------------------------------------------------

def get_commandline_arguments ( url, realm ):

    # parse command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument ('-d', '--debug',
                         action='store_true',
                         help='Enable debug output.')

    parser.add_argument ('--url', dest='url',
                         type=six.text_type,
                         default=url,
                         help='The router URL (default: "ws://masterdns.kikis.local:8080/ws").')

    parser.add_argument ('--realm',
                         dest='realm',
                         type=six.text_type,
                         default=realm,
                         help='The realm to join (default: "realm1").')

    return parser.parse_args()


#----------------------------------------------------------------------------------

if __name__ == '__main__':

#----------------------------------------------------------------------------------

    # default values for commandline arguments
    url   = "ws://masterdns.kikis.local:8080/ws"
    realm = "realm1"
    args = get_commandline_arguments ( url, realm )


    # start logging
    if args.debug:
        txaio.start_logging(level='debug')
    else:
        txaio.start_logging(level='info')


#----------------------------------------------------------------------------------

    # dictionary argument to 'get()'

    # hop to the vim entry
    vs_dict = {
        u'0': u'com.kikis.get',
        u'1': u'UIA_NameProperty',
        u'2': u'Taskbar',
        u'3': u'UIA_NameProperty',
        u'4': u'Running applications',
        u'5': u'UIA_NameProperty',
        u'6': u'Visual Studio 2017 - 1 running window',
        u'7': u'get',
        u'8': u'UIA_IsKeyboardFocusableProperty'
    }
        #u'8': u'UIA_IsEnabledProperty'
        #u'8': u'UIA_IsEnabledProperty'
        #u'8': u'UIA_IsKeyboardFocusableProperty'
        #u'8': u'UIA_HasKeyboardFocusProperty'
        #u'8': u'UIA_NameProperty'

    nav_dict = vs_dict

#----------------------------------------------------------------------------------

    res = get( args, nav_dict )

    print('----------------------------')
    print(' get returns res =', res)
    print('----------------------------')


#----------------------------------------------------------------------------------


print('----------------------------')
print(u'out of the main block')
print('----------------------------')
