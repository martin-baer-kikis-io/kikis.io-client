
#-----------------------------------------------------------

"""

    my_app.py

        Test application testing a 'get' then a 'set' 
        operation for a kikis client application.

        Date: 04/28/2020.

        Notes:  just starting on the 'set' side of the
        project.  This version of the app will get a value
        from the ControlPattern object and tne in
        python, manipulate the string, then write it
        to the control pattern from which it caame.       


"""

#-----------------------------------------------------------

#import time
#from autobahn.twisted.util import sleep

from kikis.getter_setter_03_20 import get_element_value
from kikis.getter_setter_03_20 import set_element_value

#-----------------------------------------------------------

if __name__ == '__main__':

    sub = "__main__"
    print ('\n\n\n>>> entering ', sub )

#-----------------------------------------------------------

    # define 'path'. This creates a resuable path to a specific
    # element in the remote host's UI Tree.

    path  = []

    # using UIAutomation Elements
    #path.append({ u'UIA_NameProperty' : u'SetTestFile - Notepad' })
    #path.append({ u'UIA_NameProperty' : u'Text Editor' })

    # using inspect tags
    path.append({ u'Name' : u'SetTestFile - Notepad' })
    path.append({ u'Name' : u'Text Editor' })

#-----------------------------------------------------------

    # get and set values in the remote UI Tree. 
    #
    # format:
    #
    #   [u'get' | u'set'], [inspect.exe name string ], [path to element] 
    #

    # create get/set stanza for the target element/control

    # How found  - skipping, probably an Inspct artifact...
    g = []
    g.append({ u'get' : u'How found' })
    g.extend( path )


    # Name

    g = []
    #g.append({ u'get' : u'Name' })
    g.append({ u'get' : u'UIA_NameProperty' })
    g.extend( path )

    res = get_element_value( g )
    print(sub, ' RESULT: ', res)

    print( ' exitiing...' )
    exit()


    # ControlType
    g = []
    g.append({ u'get' : u'ControlType' })
    g.extend( path )
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)

    g = []
    g.append({ u'get' : u'LocalizedControlType' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'BoundingRectangle' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsEnabled' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsOffscreen' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsKeyboardFocusable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'HasKeyboardFocus' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'AccessKey' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'ProcessId' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'RuntimeId' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'AutomationId' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'ProviderDescription' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsPassword' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'ItemStatus' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'HelpText' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.ChildId' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.DefaultAction' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.Help' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.KeyboardShortcut' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.Name' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.Role' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.State' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LegacyIAccessible.Value' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsAnnotationPatternAvailable' })
    g.extend( path ) 
    
    
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsDragPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsDockPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsDropTargetPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsExpandCollapsePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsGridItemPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsGridPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsInvokePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsItemContainerPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsLegacyIAccessiblePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsMultipleViewPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsObjectModelPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsRangeValuePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsScrollItemPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsScrollPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsSelectionItemPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsSelectionPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsSpreadsheetItemPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsSpreadsheetPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsStylesPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsSynchronizedInputPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTableItemPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTablePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTextChildPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTextEditPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTextPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTextPattern2Available' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTogglePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTransformPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsTransform2PatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsValuePatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsVirtualizedItemPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsWindowPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsCustomNavigationPatternAvailable' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'IsSelectionPattern2Available' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'FirstChild' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'LastChild' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'Next' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'Previous' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'Other Props' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'Children' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)
    g = []
    g.append({ u'get' : u'Ancestors' })
    g.extend( path ) 
    res = get_element_value( g ) 
    print(sub, ' RESULT: ', res)


#-----------------------------------------------------------
