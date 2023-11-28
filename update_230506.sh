#!/bin/bash

rm -rf /tmp/jethexa_update
set -e

mkdir /tmp/jethexa_update
tar xf update_230506.tar.gz -C /tmp/jethexa_update --strip-components 1

set -v

rm -rf /home/hiwonder/jethexa/src/jethexa_controller
rm -rf /home/hiwonder/jethexa/src/jethexa_sdk
rm -rf /home/hiwonder/jethexa/src/lab_config

mv /tmp/jethexa_update/jethexa_controller /home/hiwonder/jethexa/src
mv /tmp/jethexa_update/jethexa_sdk /home/hiwonder/jethexa/src
mv /tmp/jethexa_update/lab_config /home/hiwonder/jethexa/src

rm -rf /tmp/jethexa_update

