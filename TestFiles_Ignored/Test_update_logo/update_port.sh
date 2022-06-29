# https://lindevs.com/install-jq-on-ubuntu/

printf(jq '.school_name_db' system_config.json)
#.school_name_db


echo 1 | sudo -S python3 -m http.server 41200