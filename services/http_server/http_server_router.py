import sys
import re
import json

class Router():

    routes = [{'path' : '^\/.+\.[png|jpg|css]' , 'service' : 'http_server_ressource'},
              {'path' : '^\/.+\.[js]' , 'service' : 'http_server_script'},
              #{'path' : '^\/sentences$'           , 'service' : 'sentences_list'},
              {'path' : '^\/$'                    , 'service' : 'http_server_view'}]

    def __init__(self, services):
        self.services = services

    def do_GET(self, path, args):
        for route in self.routes:
            if (re.match(route['path'], path)):
                return self.services.get(route['service']).get(path, args)
        return False

    def do_POST(self, path, args):
        for route in self.routes:
            if (re.match(route['path'], path)):
                return self.services.get(route['service']).add(path, args)
        return False

    def do_DELETE(self, path, args):
        for route in self.routes:
            if (re.match(route['path'], path)):
                return self.services.get(route['service']).delete(path, args)
        return False

    def do_VOTE(self, path, args):
        for route in self.routes:
            if (re.match(route['path'], path)):
                return self.services.get(route['service']).vote(path, args)
        return False


