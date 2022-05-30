cd ~
cd Downloads/
echo 1 | sudo -S rm API_TOKEN.txt
echo 1 | sudo -S rm API_TOKEN\ \(1\).txt
echo 1 | sudo -S rm API_TOKEN\ \(2\).txt
echo 1 | sudo -S rm API_TOKEN\ \(3\).txt
echo 1 | sudo -S rm API_TOKEN\ \(4\).txt
echo 1 | sudo -S rm API_TOKEN\ \(5\).txt
echo 1 | sudo -S rm API_TOKEN\ \(6\).txt
echo 1 | sudo -S rm API_TOKEN\ \(7\).txt
echo 1 | sudo -S rm API_TOKEN\ \(8\).txt
echo 1 | sudo -S rm API_TOKEN\ \(9\).txt
cd ~
sleep 3
chromium-browser --start-fullscreen --app=http://localhost:41200