echo "Cloning Repo...."
git clone https://github.com/tajmobile1/TajLinkshortenerbot.git /TajLinkshortenerbot
cd /TajLinkshortenerbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
