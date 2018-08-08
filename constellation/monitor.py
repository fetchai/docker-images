#!/usr/bin/env python3
import subprocess
import time
import sys

APPLICATION = '/app/constellation'


def output(text):
	sys.stderr.write(text + '\n')
	sys.stderr.flush()


while True:
	output('Starting application...')
	exit_code = subprocess.call([APPLICATION])

	if exit_code == 0:
		output('Stopping application...')
		break

	output('Sleeping...')

	time.sleep(30)

	output('Restarting application...')
