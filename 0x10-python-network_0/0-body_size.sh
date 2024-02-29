#!/bin/bash

# Get the URL from the command line argument
url="$1"

# Check if URL is provided
if [ -z "$url" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Send request using curl in silent mode and capture response body
response=$(curl -s "$url")

# Get body size using wc -l (word count)
size=$(echo "$response" | wc -l)

# Display the size in bytes, handling potential errors
if [ $? -eq 0 ]; then
  echo "Size: $size bytes"
else
  echo "Error: Failed to retrieve response from $url."
  exit 1
fi

