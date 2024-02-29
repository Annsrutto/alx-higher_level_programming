#!/bin/bash
# This script takes a URL as input, sends a request using curl, and displays the size of the response body in bytes.

URL=$1
SIZE=$(curl -s "$URL" | wc -c)
echo "$SIZE"
