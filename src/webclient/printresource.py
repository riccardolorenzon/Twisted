'''
Created on 10/set/2014

@author: riccardo
'''
from twisted.internet import reactor 
from twisted.web.client import getPage 
import sys

def printPage(result): 
    print result
    
def printError(failure):
    print >>sys.stderr, failure
    
def stop(result): 
    reactor.stop()  # @UndefinedVariable

if len(sys.argv) != 2:
    print >>sys.stderr, "Usage: python print_resource.py <URL>" 
    exit(1)

d = getPage(sys.argv[1])
d.addCallbacks(printPage, printError)
d.addBoth(stop)
reactor.run()  # @UndefinedVariable
