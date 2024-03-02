#!/bin/bash

error_log="./error.log"
echo -n "" > "$error_log" # Clear the error log

while true; do
	echo "Starting bot"
	python3 main.py 2>> "$error_log"
	
	# Check the exit status of the Python program
	if [ $? -eq 0 ]; then
		echo "Program exited normally."
		break
	else
		echo "Program exited with an error. Restarting..."
		sleep 1  # small delay before restarting
	fi

	echo "" >> "$error_log"  # Add a new line in the error log
done
