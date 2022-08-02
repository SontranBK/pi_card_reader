cd ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/main_NFC_Mifare.py ~
echo 1 | sudo -S cp pi_card_reader/Python_Backend/service-account.json ~
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
# Check if API_TOKEN.txt exists
# Wait 2 sec * 50 = 100 secs 
count=0
while [ $count -le 50 ];
do
    if [ -f "API_TOKEN.txt" ]; 
	then
		# if file exist, then run python right away
		echo "API_TOKEN exists"
		break
	else
		# is it is not exist then it will be printed
		#echo "No API_TOKEN found"
		count=$((count+1))
		#echo $count
		sleep 2
	fi
done  
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
echo 1 | sudo -S python3 main_NFC_Mifare.py