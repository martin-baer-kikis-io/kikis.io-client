//
//  kikis_exec.h
//
//

using namespace std;

// Texted based design uses a switch.  Here we assign an int to each
// IUIAutomation method name string.  Add new names, to the end of
// the list of #defines.

#define AddAutomationEventHandler					0
#define AddFocusChangedEventHandler					1
#define AddPropertyChangedEventHandler				2
#define AddPropertyChangedEventHandlerNativeArray	3
#define AddStructureChangedEventHandler				4
#define CheckNotSupported							5
#define CompareElements								6
#define CompareRuntimeIds							7
#define CreateAndCondition							8
#define CreateAndConditionFromArray					9
#define CreateAndConditionFromNativeArray			10	
#define CreateCacheRequest							11
#define CreateFalseCondition						12
#define CreateNotCondition							13
#define CreateOrCondition							14
#define CreateOrConditionFromArray					15
#define CreateOrConditionFromNativeArray			16
#define CreatePropertyCondition						17
#define CreatePropertyConditionEx					18
#define CreateProxyFactoryEntry						19
#define CreateTreeWalker							20
#define CreateTrueCondition							21
#define ElementFromHandle							22
#define ElementFromHandleBuildCache					23
#define ElementFromIAccessible						24
#define ElementFromIAccessibleBuildCache			25
#define ElementFromPoint							26
#define ElementFromPointBuildCache					27
#define GetFocusedElement							28	
#define GetFocusedElementBuildCache					29
#define GetPatternProgrammaticName					30
#define GetPropertyProgrammaticName					31
#define GetRootElement								32
#define GetRootElementBuildCache					33
#define IntNativeArrayToSafeArray					34
#define IntSafeArrayToNativeArray					35
#define PollForPotentialSupportedPatterns			36
#define PollForPotentialSupportedProperties			37
#define RectToVariant								38
#define RemoveAllEventHandlers						39
#define RemoveAutomationEventHandler				40
#define RemoveFocusChangedEventHandler				41
#define RemovePropertyChangedEventHandler			42
#define RemoveStructureChangedEventHandler			43
#define SafeArrayToRectNativeArray					44
#define VariantToRect								45

// last element in function names vector
#define FNAMES_LAST									45
