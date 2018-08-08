#!/usr/bin/env python3
import subprocess
import time
import sys
import requests

APPLICATION = '/app/constellation'


def output(text):
    sys.stderr.write(text + '\n')
    sys.stderr.flush()


# find out external ip address
public_ip = requests.get('https://api.ipify.org').text
print('Public IP: ', public_ip)

n = 0
while True:
    output('Starting application...')

    with open('/app/node-{}.log'.format(n), 'w') as node_log:

        # run the application
        exit_code = subprocess.call([APPLICATION, '-bootstrap', public_ip], stdout=node_log, stderr=subprocess.STDOUT)

        if exit_code == 0:
            output('Stopping application...')
            break

    output('Sleeping...')

    time.sleep(30)
    n += 1

    output('Restarting application...')
