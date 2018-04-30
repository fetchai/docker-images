#!/bin/bash
set -e

cd ${0%/*}
. ./docker-env-common.sh

"$(dirname "$(pwd)")"

