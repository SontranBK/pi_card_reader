
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
              