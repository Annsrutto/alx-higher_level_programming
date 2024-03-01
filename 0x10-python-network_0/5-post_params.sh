#!/bin/bash
# Send a POST request using curl with specific parameters and display the body of the response
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
