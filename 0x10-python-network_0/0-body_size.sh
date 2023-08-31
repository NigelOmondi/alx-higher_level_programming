#!/bin/bash
# Takes in URL, sends a request to the URL
# and displays the size of the body of response.
curl -s "$1" | wc -c
