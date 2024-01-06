#!/bin/bash
#working on json post req
curl -sX "POST"  "$1" -H "Content-Type: application/json" -d @$2
