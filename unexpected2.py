import sys

if len(sys.argv) == 1:
    # Prints:
    #   called 2: hey
    #   called 3: None
    #
    # instead of the probably expected
    #   called 2: hey
    #   called 3: hey
    from twisted.internet import defer
else:
    # Prints:
    #   called 2: hey
    #   called 3: hey
    import tdefer as defer


def report2(result):
    print 'called 2:', result

def report3(result):
    print 'called 3:', result

d1 = defer.Deferred()
d2 = defer.Deferred().addCallback(report2)
d3 = defer.Deferred().addCallback(report3)

d1.chainDeferred(d2)
d1.chainDeferred(d3)

d1.callback('hey')
