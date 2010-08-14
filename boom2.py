import sys

if len(sys.argv) == 1:
    # Raises defer.AlreadyCalledError because calling d1.callback will call
    # d2, which has already been called.
    from twisted.internet import defer
else:
    # Raises AssertionError: Can't callback an already chained deferred
    # because calling callback on a deferred that's already been chained is
    # asking for trouble (as above).
    import tdefer as defer

d1 = defer.Deferred()
d2 = defer.Deferred()
d1.chainDeferred(d2)
d2.callback('hey')
d1.callback('jude')
