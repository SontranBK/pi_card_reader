# Install PCSCD AB Circle support lib
cd ~
sudo apt-get install swig
sudo apt-get install libpcsclite-dev
sudo apt-get install pcscd
sudo python3 -m pip install pyscard
yaourt -S aur/acsccid
sudo systemctl enable pcscd.service
sudo systemctl start pcscd.service 
sudo systemctl status pcscd.service
# Remove old repo and download new one, also install jq lib
cd ~
echo 1 | sudo -S rm -r pi_card_reader/
cd ~
sudo apt update
sudo apt install -y jq
jq --version
cd ~
sudo apt install git
cd ~
git clone https://github.com/SontranBK/pi_card_reader
# Run pub get to get all the dependencies listed in the pubspec.yaml file
# If the system cache doesn’t already contain the dependencies, pub get updates the cache, downloading dependencies if necessary
cd pi_card_reader/
sudo flutter pub get
# Check config file and copy new one 
cd ~
if [ -f "system_config.json" ]; 
then
    # if file exist, then pass
    echo "Config file already exists"
    break
else
    cp pi_card_reader/Tools_And_Docs/system_config.json ~
    cd ~
fi
sudo modprobe usbserial vendor=1a86 product=7532