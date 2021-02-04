
from os import environ


# JUST a SKETCH - might be useful


class HopList(list):

    """
    An class for lists of UIAutomation Tree Hops

    Example usage:

        a = HopList((1,2,3), 35, 22)

        print(a)
        for x in a:
            print(x)

    """

    sub = u"HopList"
    print("Entering ", sub )

    def __init__(self, *args):
        super(HopList, self).__init__(args[0])

        # Do something with the other args (and potentially kwars)
        # add support for rpc_url and such...
