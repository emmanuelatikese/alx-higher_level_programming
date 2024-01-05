#!/bin/bash
#checking for allows
echo '$1' | xargs curl -sI | grep Allow | cut -d " " -f 2-
