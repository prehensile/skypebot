#!/bin/bash
while true
do
	python skypebot.py
	rc=$? 
	echo $rc
	if [[ $rc == 3 ]]
	then
		echo Updating...	
		git pull
		sleep 15
	else
		echo Exit.
		break
	fi
done
