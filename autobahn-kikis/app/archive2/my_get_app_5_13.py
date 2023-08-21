
from kikis.IUIAutomation_5_13 import get


INPUT_ARRAY_SIZE = 16

#----------------------------------------------------------------------------------

"""

    my_app.py

        Test application for the get() command


"""

#----------------------------------------------------------------------------------

if __name__ == '__main__':

#----------------------------------------------------------------------------------

    # test data
    #ld.append({ u'get' : u'UIA_NameProperty' })
    #ld.append({ u'get' : u'UIA_TextPatternId' })
    #ld.append({ u'get' : u'UIA_IsEnabledProperty' })
    #ld.append({ u'get' : u'UIA_HasKeyboardFocusProperty'})
    #ld.append({ u'get' : u'UIA_IsKeyboardFocusableProperty' })

#----------------------------------------------------------------------------------

    #  define a path from root to the target property or pattern

    vs_path  = []
    vs_path.append({ u'UIA_NameProperty' : u'Taskbar' })
    vs_path.append({ u'UIA_NameProperty' : u'Running applications' })
    vs_path.append({ u'UIA_NameProperty' : u'Visual Studio 2017 - 1 running window' })

#----------------------------------------------------------------------------------

    # create new list with 'get' as first element and append target circut
    nm = []
    nm.append({ u'get' : u'UIA_NameProperty' })
    nm.extend( vs_path )

#----------------------------------------------------------------------------------

    # create new list with 'get' as first element and append target circut
    fo = []
    fo.append({ u'get' : u'UIA_HasKeyboardFocusProperty'})
    fo.extend( vs_path )

#----------------------------------------------------------------------------------

    # call get and print the result
    #res1 = get( args, nm )

    #res1 = get( nm )
    #print(' RESULT: ', res1)

    res2 = get( fo )
    print(' RESULT: ', res2)

#----------------------------------------------------------------------------------

