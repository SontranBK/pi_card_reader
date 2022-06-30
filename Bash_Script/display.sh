cd ~
sleep 3
chromium-browser --start-fullscreen --app=http://localhost:$(jq ".web_port" system_config.json)