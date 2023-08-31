#!/bin/bash
# Takes in URL, sends a GET request to the URL
# and displays body of 200 status code responses.
curl -sL "$1"
