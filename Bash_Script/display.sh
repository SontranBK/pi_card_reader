cd ~
cd Downloads/
echo 1 | sudo -S rm API_TOKEN.txt
cd ~
sleep 180
chromium-browser --start-fullscreen --app=http://localhost:41200
