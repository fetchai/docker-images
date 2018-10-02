#!/usr/bin/env python3
import subprocess
import time
import sys
import os
import json
import requests
import base64

APPLICATION = '/app/constellation'


def output(text):
    sys.stderr.write(text + '\n')
    sys.stderr.flush()


# get the initial configuration from the environment variable
config = os.environ.get('CONSTELLATION_CONFIG')

if config is None:
    output('Configuration not specified')
else:

    # decode the configuration
    config = base64.b64decode(config)
    output('Config: ' + config)

    # json parse the config
    config = json.loads(config)

# run the main application
subprocess.check_call([APPLICATION, '-mine'])

# find out external ip address
# public_ip = requests.get('https://api.ipify.org').text
# output('Public IP: ', public_ip)

# n = 0
# while True:
#     output('Starting application...')

#     with open('/app/node-{}.log'.format(n), 'w') as node_log:

#         # run the application
#         exit_code = subprocess.call([APPLICATION, '-mine'], stdout=node_log, stderr=subprocess.STDOUT)

#         if exit_code == 0:
#             output('Stopping application...')
#             break

#     output('Sleeping...')

#     time.sleep(30)
#     n += 1

#     output('Restarting application...')
