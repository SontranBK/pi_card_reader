cd ~
cd pi_card_reader/
echo 1 | sudo -S rm -r build/
cd ~
cd pi_card_reader/
echo 1 | sudo -S flutter build web --release --web-renderer html
cd ~
echo 1 | sudo -S cp pi_card_reader/assets/Meta_edu.png pi_card_reader/build/web/assets/
echo 1 | sudo -S cp pi_card_reader/assets/Meta_edu.png pi_card_reader/build/web/assets/assets/