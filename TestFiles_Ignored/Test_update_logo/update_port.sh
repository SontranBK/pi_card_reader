# https://lindevs.com/install-jq-on-ubuntu/

echo 1 | sudo -S python3 -m http.server $(jq ".web_port" system_config.json)

chromium-browser --start-fullscreen --app=http://localhost:$(jq ".web_port" system_config.json)