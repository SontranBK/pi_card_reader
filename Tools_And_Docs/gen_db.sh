#!/bin/bash
# This is not a file used to run program, but a tool
# use this tool to create local database for each month
echo -n "Enter a number: "
read month
echo "Bash version ${BASH_VERSION}..."
for day in {1..31}
do 
    echo "Day: $day"
    if [[ $day -lt 10 ]]
    then
    	cp LH_local_db.db 0${day}_${month}_2022.db
	else
		cp LH_local_db.db ${day}_${month}_2022.db
	fi



done