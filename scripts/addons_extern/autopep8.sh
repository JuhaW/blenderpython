#!/bin/bash

for file in *.py ; do
    echo "Cleaning '$file'"
    autopep8 --in-place -a -a --ignore=E501,E711,E712 "$file"

done
