from twisted.python import usage
from twisted.python import reflect
import sys

class Options(usage.Options):

    # define a list of subcommands for the options class
    subCommand = [
        ["run", None, usage.Options, "Run the worker"],
        ["synposis", None, usage.Options, "Print the synposis"],
        ["help", None, usage.Options, "Print the help"],
        ["stop", None, usage.Options, "Stop the worker"],
        ["restart", None, usage.Options, "Restart the worker"]
    ]

    synposis = "Hello world"

    def opt_version(self):
        return super().opt_version()
    
    def postOptions(self):
        if not hasattr(self, 'subOptions'):
            raise usage.UsageError("You must specify a subcommand")

def run():

    config = Options()

    try:
        config.parseOptions()
    except usage.UsageError as e:
        print("{}:  {}".format(sys.argv[0], e))
        print()
        c = getattr(config, 'subOptions', config)
        print(str(c))
        sys.exit(1)

    subConfig = config.subOptions
    subCommandFunction = reflect.namedObject(subConfig.subcommandFunction)
    sys.exit(subCommandFunction(subConfig))