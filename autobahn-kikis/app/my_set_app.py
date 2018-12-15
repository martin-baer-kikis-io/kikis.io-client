
import os
import argparse
import six
import txaio

#from kikis.Constants import *
from kikis.IUIAutomation import set

INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

"""

    my_set_app.py

        Test application for the set() command


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

    # list argument to 'get()'

    # initialize a list with NULL's
    nav_list = [u'NULL'] * INPUT_ARRAY_SIZE

    nav_list[0]    = u'com.kikis.set'
    nav_list[1]    = u'UIA_NameProperty'
    nav_list[2]    = u'Taskbar'
    nav_list[3]    = u'UIA_NameProperty'
    nav_list[4]    = u'Running applications'
    nav_list[5]    = u'UIA_NameProperty'
    nav_list[6]    = u'Visual Studio 2017 - 1 running window'
    nav_list[7]    = u'set'
    nav_list[8]    = u'UIA_IsKeyboardFocusableProperty'

    #nav_list[8]    = u'UIA_NameProperty'
    #nav_list[8]    = u'UIA_IsEnabledProperty'
    #nav_list[8]    = u'UIA_IsEnabledProperty'
    #nav_list[8]    = u'UIA_IsKeyboardFocusableProperty'
    #nav_list[8]    = u'UIA_HasKeyboardFocusProperty'
    #nav_list[8]    = u'UIA_NameProperty'

#----------------------------------------------------------------------------------

    res = set( args, nav_list )

    print('----------------------------')
    print(' set returns res =', res)
    print('----------------------------')


#----------------------------------------------------------------------------------


print('----------------------------')
print(u'out of the main block')
print('----------------------------')
