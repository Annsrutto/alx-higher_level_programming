#!/bin/bash
# Make a request to cause the server to respond with "You got me!" in the body of the response.
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
