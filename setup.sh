sudo apt install python3-pip
sudo /usr/bin/python3 -m pip install --upgrade pip
sudo pip3 install enquiries
sudo pip3 install requests
sudo pip3 install colorama

cd Tools/torghost
./build.sh

echo Process finish, now you can run delvedleak.py