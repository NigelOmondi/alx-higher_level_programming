#!/bin/bash
# Takes in URL, sends a GET request to URL
# and displays body of 200 status code responses.
curl -sL "$1"
