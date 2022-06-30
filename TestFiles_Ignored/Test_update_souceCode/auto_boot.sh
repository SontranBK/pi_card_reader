lastTag=$(git tag --sort=committerdate | tail -1)
currentTag=$(git describe --tags)

echo The last version is ${lastTag}
echo The current version is $currentTag

# echo "Do you want to update this version? (y/n)"
# read action
# check='y'
# if [ $action = $check ]

if [ $lastTag != $currentTag ] 
then	
	#echo Enter your repository name:
	#read nameRepo
	#echo Your Repository is ${nameRepo}
	
	cd .. 
	# mv -T pi_card_reader pi_card_reader_${currentTag}
	rm -rf pi_card_reader
	git clone --branch ${lastTag} https://github.com/SontranBK/pi_card_reader 
fi

title1="Initializing User Interface"
title2="Opening User Interface"
title3="Connecting to NFC Reader"
title4="Retry server"

cmd1="sh generate_UI.sh"
cmd2="sh display.sh"
cmd3="sh backend_NFC.sh"
cmd4="sh backend_retryServer.sh"


cd ~
cd pi_card_reader/Bash_Script/
gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
	       --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" \
               --tab --title="$title4" --command="bash -c '$cmd4; $SHELL'" 
              