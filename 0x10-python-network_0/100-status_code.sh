#!/bin/bash
# displays status code of the response.
curl -s - /dev/null -w "%{http_code}" "$1"
