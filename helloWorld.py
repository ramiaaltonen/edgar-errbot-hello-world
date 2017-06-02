from errbot import BotPlugin, botcmd

class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Says hello!"""
        return "Hello, world! "
