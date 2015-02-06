'''
Created on 12/set/2014

@author: riccardo
'''
from twisted.internet import reactor, protocol 
from twisted.words.protocols import irc
import sys

class EchoBot(irc.IRCClient): 
    nickname = "echobot"
    def signedOn(self):
        # Called once the bot has connected to the IRC server 
        self.join(self.factory.channel)
        
    def privmsg(self, user, channel, msg):
        # Despite the name, called when the bot receives any message, # be it a private message or in a channel.
        user = user.split('!', 1)[0]
        if channel == self.nickname:
            # This is a private message to me; echo it.
            self.msg(user, msg)
        elif msg.startswith(self.nickname + ":"):
            # This message started with my nickname and is thus
            # directed at me; echo it.
            self.msg(channel, user + ":" + msg[len(self.nickname + ":"):])
            
    def action(self, user, channel, action):
        # Called when a user in the channel takes an action (e.g., "/me # dances"). Imitate the user.
        self.describe(channel, action)
        
class EchoBotFactory(protocol.ClientFactory): 
    
    def __init__(self, channel):
        self.channel = channel

    def buildProtocol(self, addr): 
        proto = EchoBot() 
        proto.factory = self 
        return proto

    def clientConnectionLost(self, connector, reason): # Try to reconnect if disconnected. 
        connector.connect()
    def clientConnectionFailed(self, connector, reason): 
        reactor.stop()  # @UndefinedVariable

network = sys.argv[1]
port = int(sys.argv[2])
channel = sys.argv[3]

reactor.connectTCP(network, port, EchoBotFactory(channel))  # @UndefinedVariable
reactor.run()  # @UndefinedVariable