#!/bin/bash
#looking or status
curl -s "$1" -w "%{http_code}" -o /dev/null
