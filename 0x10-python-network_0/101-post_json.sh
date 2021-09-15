#!/bin/bash
# curl JSON
curl -sX POST "$1" -H "Content-Type: application/json" -d "`cat $2`"
