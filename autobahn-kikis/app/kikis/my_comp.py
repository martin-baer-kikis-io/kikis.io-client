from os import environ
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    """
    An application component using the time service.
    """
    sub = u"Component CTor"
    print("Entering ", sub )

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")

        extra = self.config.extra
        rpc_url  = next(iter(extra.keys()))
        a = next(iter(extra.values()))

        #print("--------------------------------------------------------------------")
        #print("url: ", rpc_url)
        #print("a: ", a )
        #print("--------------------------------------------------------------------")
#
#        try:
#            now = yield self.call(u'com.timeservice.now')
#        except Exception as e:
#            print("Error: {}".format(e))
#        else:
#            print("Current time from time service: {}".format(now))
#
#        self.leave()
#
#
#
        try:
            #res = yield session.call(u'com.myapp.add2', 2, 3)
            #res = yield session.call(
            res = yield self.call(
                  rpc_url, a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7],
                  a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], u'NULL'
                  )

            #print(' my_comp::onJoin returns res =', res)
            #print('----------------------------')

            self.config.extra[u'result'] = res

            self.leave()
            #self.disconnect()
            #yield self.leave()
            #self.disconnect()


        except Exception as e:
            print("call error: {0}".format(e))
            print("calling leave in exception block")
            self.leave()


    def onDisconnect(self):
        print("disconnected")
        reactor.stop()
