
from kikis.getter_setter import get_element_value

#----------------------------------------------------------------------------------

"""

    my_get_app.py

        Test application for the 'get' command


"""

#----------------------------------------------------------------------------------

if __name__ == '__main__':

    sub = "__main__"
    print ('\n\n\n>>> entering ', sub )

#----------------------------------------------------------------------------------

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

    # call get_element_value() and print the result

    print('>>> calling get_element_value...' )

    print('>>> calling first time: ')
    res1 = get_element_value( nm )
    print(sub, ' RESULT 1: ', res1)

    #print('>>> calling same values, second time: ')
    #res1 = get_element_value( nm )
    #print(sub, ' RESULT 1: ', res1)

    #print('--------------------------------------------------------------------------------')

    #print('calling second time: ')
    #res2 = get_element_value( fo )
    #print('RESULT 2: ', res2)

    #print('--------------------------------------------------------------------------------')


#----------------------------------------------------------------------------------

    # other test data
    #ld.append({ u'get' : u'UIA_NameProperty' })
    #ld.append({ u'get' : u'UIA_TextPatternId' })
    #ld.append({ u'get' : u'UIA_IsEnabledProperty' })
    #ld.append({ u'get' : u'UIA_HasKeyboardFocusProperty'})
    #ld.append({ u'get' : u'UIA_IsKeyboardFocusableProperty' })

#----------------------------------------------------------------------------------
