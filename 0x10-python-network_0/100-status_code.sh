#!/bin/bash
# Sends a JSON POST request and displays
# body of the response.
curl -s - /dev/null -w "%{http_code}" "$1"
