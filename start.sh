#!/bin/bash
if [ $# -eq 2 ]
then
	cd Code
	
	python3 choreography.py
	python2 robot.py $1 $2
else
  echo 'parameter not valid'

fi
