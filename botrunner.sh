#!/bin/bash
while true
do
	python skypebot.py
	rc=$? 
	echo $rc
	if [[ $rc != 100 ]]
	then
		echo Updating...	
		git pull
		sleep 10
	else
		echo Exit.
		break
	fi
done