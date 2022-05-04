cd ~
echo 1 | sudo -S rm /home/thien-nv/Downloads/API_TOKEN.txt
sleep 180
chromium-browser --start-fullscreen --app=http://localhost:41200
