#!/bin/bash
#checking for allows
curl -sI "$1" | awk '/Allow/ {print $2}'
