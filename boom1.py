import sys

if len(sys.argv) == 1:
    # With normal deferreds, this raises defer.AlreadyCalledError because
    # the callback of d1 causes the callback of d2 to be called, but d2 has
    # already been cancelled (and hence called).
    from twisted.internet import defer
else:
    # With tdefer.py, there is no error because d1.callback will not call
    # d2 as it has already been cancelled.
    import tdefer as defer

def printCancel(fail):
    fail.trap(defer.CancelledError)
    print 'cancelled'

def canceller(d):
    print 'cancelling'
    
d1 = defer.Deferred()
d2 = defer.Deferred(canceller)
d2.addErrback(printCancel)
d1.chainDeferred(d2)
d2.cancel()
d1.callback('hey')
