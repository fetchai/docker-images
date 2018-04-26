#!/bin/bash

cd ${0%/*}
. ./docker-env-common.sh
. ./docker-common.sh

"$(dirname "$(pwd)")"
