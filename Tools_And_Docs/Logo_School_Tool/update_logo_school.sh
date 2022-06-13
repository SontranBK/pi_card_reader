cd ~
cd pi_card_reader/
echo 1 | sudo -S rm -r build/
cd ~
cd pi_card_reader/
echo 1 | sudo -S flutter build web
cd ~
echo 1 | sudo -S cp pi_card_reader/build/web/assets/assets/logo.png pi_card_reader/build/web/assets/