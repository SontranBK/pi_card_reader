title1="tab 1"
title2="tab 2"
title3="tab 3"

cmd1="sh generate_UI.sh"
cmd2="sh display.sh"
cmd3="sh backend_NFC.sh"

gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
               --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" 

