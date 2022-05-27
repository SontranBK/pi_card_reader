cd ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/main_NFC_Mifare_DU950.py ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/service-account.json ~
sleep 20
echo 1 | sudo -S python3 main_NFC_Mifare_DU950.py
