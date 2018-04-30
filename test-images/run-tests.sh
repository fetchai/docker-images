#!/bin/bash

set -e
pwd
"${0%/*}"/test-default-env-setup/run-test.sh
"${0%/*}"/test-custom-env-setup/run-test.sh
echo "=========> TEST PASSED <========="

