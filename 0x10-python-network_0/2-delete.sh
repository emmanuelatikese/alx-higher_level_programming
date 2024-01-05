#!/bin/bash
#deleting all that's required
echo "$1" | xargs curl -sX DELETE
