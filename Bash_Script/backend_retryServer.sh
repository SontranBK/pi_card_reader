cd ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/main_retry_server.py ~
sleep 50
echo 1 | sudo -S python3 main_retry_server.py
