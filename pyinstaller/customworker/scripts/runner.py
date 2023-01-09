from twisted.python import usage

class Options(usage.Options):

    synposis = "Hello world"

def run():

    config = Options()

    print("Hello world")