#!/usr/bin/env python3
import subprocess
import time
import sys

APPLICATION = '/app/constellation'


def output(text):
	sys.stderr.write(text + '\n')
	sys.stderr.flush()


n = 0
while True:
	output('Starting application...')

	with open('/app/node-{}.log'.format(n), 'w') as node_log:

		# run the application
		exit_code = subprocess.call([APPLICATION], stdout=node_log, stderr=subprocess.STDOUT)

		if exit_code == 0:
			output('Stopping application...')
			break

	output('Sleeping...')

	time.sleep(30)
	n += 1

	output('Restarting application...')
