#!/bin/bash
#Send a JSON POST request to a URL with the contents of a file in the body and display the response body.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
