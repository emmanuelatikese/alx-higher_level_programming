#!/bin/bash
#trying to get the content-length
echo "$1" | xargs curl -s | wc -c
