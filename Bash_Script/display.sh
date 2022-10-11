cmd3="sh backend_NFC.sh"
x-terminal-emulator --new-tab --command="bash -c '$cmd3; $SHELL'" 


cd ~
sleep 3
chromium-browser --start-fullscreen --app=http://localhost:$(jq ".web_port" system_config.json)
