'''
Created on 12/set/2014

@author: riccardo
'''
import time

from twisted.internet import reactor, threads
from twisted.internet.task import LoopingCall

def blockingApiCall(arg): 
    time.sleep(1)
    return arg

def nonblockingCall(arg):
    print arg

def printResult(result):
    print result 

def finish():
    reactor.stop()  # @UndefinedVariable

d = threads.deferToThread(blockingApiCall, "Goose")
d.addCallback(printResult)
LoopingCall(nonblockingCall, "Duck").start(.25)

reactor.callLater(2, finish)  # @UndefinedVariable
reactor.run()  # @UndefinedVariable