#!/usr/bin/env python3
import subprocess
import time
import sys
import os
import json
import requests
import base64
from pprint import pformat

APPLICATION = '/app/constellation'
MANIFEST_PATH = '/app/manifest.json'


def output(text):
    sys.stderr.write(text + '\n')
    sys.stderr.flush()


def generateSection(obj):
    return { 'uri': 'tcp://{}:{}'.format(obj['externalIp'], obj['clusterNode']), 'port': obj['container'] }


# get the initial configuration from the environment variable
config = os.environ.get('CONSTELLATION_CONFIG')

cmd = [APPLICATION]

if config is None:
    output('Configuration not present - running basic miner')
    cmd += ['-mine']

else:

    # decode the configuration
    config = json.loads(base64.b64decode(config).decode())

    # create the single instance configuration
    manifest = {
        'p2p': generateSection(config['ports']['p2p']),
        'http': generateSection(config['ports']['http']),
        'lanes': [],
    }

    # append the lane information
    for lane in config['ports']['lanes']:
        manifest['lanes'].append(generateSection(lane))

    # debug configuration
    output('Config:')
    output(pformat(config))
    output('')


    output('Manifest:')
    output(pformat(manifest))
    output('')

    output('---------------------------------------------------------------------')
    output('')

    # write out the app config
    with open(MANIFEST_PATH, 'w') as manifest_file:
        json.dump(manifest, manifest_file)

    # update the cmd
    cmd += [
        '-config', MANIFEST_PATH,
        '-host-name', config['name'],
        '-token', config['token'],
        '-network-id', config['networkId'],
        '-bootstrap',
    ]

    # enable mining if told to do so
    if config.get('mining', False):
        cmd += ['-mine']

# run the main application
subprocess.check_call(cmd)

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
