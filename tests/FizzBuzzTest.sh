#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
if [[ $(sh ../FizzBuzz.sh | diff FizzBuzz.txt - ) ]]; then
echo "${RED}FAILED${NC}";
else 
echo "${GREEN}PASSED${NC}";
fi
