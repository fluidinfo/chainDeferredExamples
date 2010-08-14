import sys

if len(sys.argv) == 1:
    # Although d2 has been chained to d1, when d1 is cancelled, d2's cancel
    # method is never called. Even calling d2.cancel ourselves after the
    # call to d1.cancel has no effect, as d2 has already been called.
    from twisted.internet import defer
else:
    # With tdefer, both cancel1 and cancel2 are called when d1.cancel is
    # called. The additional final call to d2.cancel correctly has no
    # effect as d2 has been called (via d1.cancel).
    import tdefer as defer


def cancel1(d):
    print 'cancel one'
    
def cancel2(d):
    print 'cancel two'

def reportCancel(fail, which):
    fail.trap(defer.CancelledError)
    print 'cancelled', which
    
d1 = defer.Deferred(cancel1)
d1.addErrback(reportCancel, 'one')

d2 = defer.Deferred(cancel2)
d2.addErrback(reportCancel, 'two')

d1.chainDeferred(d2)
d1.cancel()

d2.cancel()
