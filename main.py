#!/usr/bin/env python
import sys
import time
import json
import os.path
import yaml
#import arrow ??

sys.path.insert(0, 'services')
sys.path.insert(0, 'services/http_server')

from time import sleep, gmtime, strftime
from http_server import *
from beautifulhue.api import Bridge

CONF_PATH = os.path.join(os.path.dirname(__file__), 'conf.yaml')

def serverCallBack(paramCallBack):
    print('call back')
    print(paramCallBack)


def test123():
    print('running ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    sleep(0.5)

if __name__ == '__main__':

    conf = []
    if (os.path.isfile(CONF_PATH)):
        with open(CONF_PATH, 'r') as conf_data:
            conf = yaml.load(conf_data.read())
    print conf
    hc1Server = HC1_Server(conf['server']['port'], serverCallBack)


    hc1Server.start()
    bridge = Bridge(device={'ip': conf['hue']['ip']}, user={'name': conf['hue']['user']})



    try:

        while (True):
            lights = bridge.light.get({'which':'all'})

            #print lights
            for light in lights['resource']:
                print (light['id'], light['name'], light['state']['on'], light['state']['bri'])
            test123()
    except KeyboardInterrupt:
        print('SigTerm received, shutting down')
        sys.exit(0)
