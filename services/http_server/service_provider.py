from http_server_router     import Router
from http_server_view       import ServeView
from http_server_script     import ServeScript
from http_server_ressource     import ServeRessource

class Singleton(type):

    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ServicesProvider(object):

    __metaclass__ = Singleton

    services      = {}

    def __init__(self, server):
        self.services['server']              = server
        self.services['http_server_view']      = ServeView(self)
        self.services['http_server_router']              = Router(self)
        self.services['http_server_script']              = ServeScript(self)
        self.services['http_server_ressource']              = ServeRessource(self)

    def has(self, service):
        if (service in self.services):
            return True
        else:
            return False

    def get(self, service):
        if (self.has(service)):
            return self.services[service]
        else:
            return False

if __name__ == "__main__":
    sp = ServicesProvider()
    print (sp)
    print sp.has('http_server_router')
    print sp.has('http_server_view')
    print sp.has('bibi')
    sp2 = ServicesProvider()
    print (sp2)