title1="Loading Process"
title2="Initializing User Interface"
title3="Opening User Interface"
title4="Connecting to NFC Reader"

cmd1="sh loading_screen.sh"
cmd2="sh generate_UI.sh"
cmd3="sh display.sh"
cmd4="sh backend_NFC.sh"

cd ~
cd pi_card_reader/Bash_Script/
gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
               --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" \
               --tab --title="$title4" --command="bash -c '$cmd4; $SHELL'" 

