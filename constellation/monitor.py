#!/usr/bin/env python3
import subprocess
import time
import sys
import os
import json
import requests
import base64
import random
from pprint import pformat

APPLICATION = '/app/constellation'
MANIFEST_PATH = '/app/manifest.json'

def output(text):
    sys.stderr.write(text + '\n')
    sys.stderr.flush()


def generateSection(obj, ip=None):
    externalIp = ip if ip is not None else obj['externalIp']
    return { 'uri': 'tcp://{}:{}'.format(externalIp, obj['clusterNode']), 'port': obj['container'] }


# add random start up delay
output('Running backoff...')
backoff = random.uniform(120.0, 360.0)
time.sleep(backoff)
output('Running backoff...complete')

# detect the public IP
public_ip = requests.get('https://api.ipify.org').text
output('Public IP: ' + public_ip)

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
        'p2p': generateSection(config['ports']['p2p'], public_ip),
        'http': generateSection(config['ports']['http'], public_ip),
        'lanes': [],
    }

    # append the lane information
    for lane in config['ports']['lanes']:
        manifest['lanes'].append(generateSection(lane, public_ip))

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
        '-network-id', str(config['networkId']),
        '-bootstrap',
    ]

    # enable mining if told to do so
    if config.get('mining', False):
        cmd += ['-mine']

# run the main application
subprocess.check_call(cmd)

