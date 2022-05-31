cd ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/main_NFC_Mifare_DU950.py ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/service-account.json ~
sleep 45
echo 1 | sudo -S rm API_TOKEN\ \(1\).txt
echo 1 | sudo -S rm API_TOKEN\ \(2\).txt
echo 1 | sudo -S rm API_TOKEN\ \(3\).txt
echo 1 | sudo -S rm API_TOKEN\ \(4\).txt
echo 1 | sudo -S rm API_TOKEN\ \(5\).txt
echo 1 | sudo -S rm API_TOKEN\ \(6\).txt
echo 1 | sudo -S rm API_TOKEN\ \(7\).txt
echo 1 | sudo -S rm API_TOKEN\ \(8\).txt
echo 1 | sudo -S rm API_TOKEN\ \(9\).txt
echo 1 | sudo -S python3 main_NFC_Mifare_DU950.py
