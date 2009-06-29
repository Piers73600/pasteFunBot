#!/bin/bash

cd $1/xml/
fl-build-report --html --output-directory=../reports/ $2
sleep 5
cd ../../reports/
current=`ls | grep -v diff | tail -1`
last=`ls | grep -v diff | tail -2 | head -1`
fl-build-report --diff $last $current
chmod -R 755 .
