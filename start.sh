if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SohanRazz/bulk-channel-link.git /bulk-channel-link

else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /bulk-channel-link
fi
cd /bulk-channel-link
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
