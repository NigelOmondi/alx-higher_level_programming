#!/bin/bash
# Takes in URL, sends GET request to URL and
# displays body of the response.
curl -sH "X-School-User-Id: 98" "$1"
