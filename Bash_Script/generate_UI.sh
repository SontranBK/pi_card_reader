cmd2="sh display.sh"
x-terminal-emulator --new-tab --command="bash -c '$cmd2; $SHELL'" 


cd ~
port=$( jq ".web_port" system_config.json )
cd ~
cd pi_card_reader/build/web/
echo 12345678 | sudo -S python3 -m http.server $port
