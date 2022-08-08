# Need to check requirement for installing libs
# Install PCSCD AB Circle support lib
cd ~
echo 1 | sudo -S apt-get install swig
echo 1 | sudo -S apt-get install libpcsclite-dev
echo 1 | sudo -S apt-get install pcscd
echo 1 | sudo -S python3 -m pip install pyscard
yaourt -S aur/acsccid
echo 1 | sudo -S systemctl enable pcscd.service
echo 1 | sudo -S systemctl start pcscd.service 
# Remove old repo and download new one, also install jq lib
cd ~
echo 1 | sudo -S -S rm -r pi_card_reader/
cd ~
echo 1 | sudo -S apt update
echo 1 | sudo -S apt install -y jq
jq --version
cd ~
echo 1 | sudo -S apt install git
cd ~
# After publishing version 1.0.3, git clone need 1.0.3 version tag
git clone https://github.com/SontranBK/pi_card_reader
# Run pub get to get all the dependencies listed in the pubspec.yaml file
# If the system cache doesn’t already contain the dependencies, pub get updates the cache, downloading dependencies if necessary
cd pi_card_reader/
echo 1 | sudo -S flutter pub get
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
echo 1 | sudo -S modprobe usbserial vendor=1a86 product=7532
