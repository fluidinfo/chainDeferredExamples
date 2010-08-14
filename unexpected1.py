import sys

if len(sys.argv) == 1:
    # Prints "called: None", instead of the probably expected "called: hey"
    from twisted.internet import defer
else:
    # Prints "called: hey"
    import tdefer as defer

def called(result):
    print 'called:', result

d1 = defer.Deferred()
d2 = defer.Deferred()
d1.chainDeferred(d2)
d1.addCallback(called)
d1.callback('hey')
