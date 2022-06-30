cd ~
port=$( jq ".web_port" system_config.json )
cd ~
cd pi_card_reader/build/web/
echo 1 | sudo -S python3 -m http.server $port
